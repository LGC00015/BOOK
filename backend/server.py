from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
import os
import logging
from pathlib import Path
from starlette.concurrency import run_in_threadpool

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

from book import assembler
from book.outline import BOOK_META, PARTS, CHAPTERS, PHASES, FIGURES, TABLES

app = FastAPI(title="Medical Devices Textbook — Production API")
api_router = APIRouter(prefix="/api")


@api_router.get("/")
async def root():
    return {"message": "Medical Devices Textbook production API", "status": "ok"}


@api_router.get("/book/meta")
async def book_meta():
    complete = sum(1 for c in CHAPTERS if c["status"] == "complete")
    status = assembler.pdf_status()
    return {
        **BOOK_META,
        "chapters_total": len(CHAPTERS),
        "chapters_complete": complete,
        "figures_count": len(FIGURES),
        "tables_count": len(TABLES),
        "pdf": status,
        "phases": PHASES,
    }


@api_router.get("/book/toc")
async def book_toc():
    parts = []
    for p in PARTS:
        parts.append({
            "num": p["num"], "title": p["title"],
            "chapters": [c for c in CHAPTERS if c["num"] in p["chapters"]],
        })
    front = [
        {"id": "cover", "title": "Cover"},
        {"id": "titlepage", "title": "Title Page"},
        {"id": "copyright", "title": "Copyright"},
        {"id": "preface", "title": "Preface"},
        {"id": "howto", "title": "How to Use This Book"},
        {"id": "syllabus", "title": "Syllabus Mapping"},
        {"id": "toc", "title": "Table of Contents"},
        {"id": "lists", "title": "Figures, Tables & Abbreviations"},
    ]
    back = [
        {"id": "glossary", "title": "Glossary"},
        {"id": "stdindex", "title": "Standards & Regulations Index"},
        {"id": "biblio", "title": "Consolidated References"},
    ]
    return {"front_matter": front, "parts": parts, "back_matter": back}


@api_router.get("/book/preview/{section_id}", response_class=HTMLResponse)
async def preview(section_id: str):
    html = await run_in_threadpool(assembler.preview_html, section_id)
    if html is None:
        raise HTTPException(status_code=404, detail="Unknown section id")
    return HTMLResponse(html)


@api_router.get("/book/pdf/status")
async def pdf_status():
    return assembler.pdf_status()


@api_router.get("/book/pdf")
async def get_pdf(variant: str = "standard"):
    if variant == "press":
        pdf, pages = await run_in_threadpool(assembler.build_press_pdf_sync)
        return Response(
            content=pdf,
            media_type="application/pdf",
            headers={
                "Content-Disposition": 'attachment; filename="Medical_Devices_Textbook_A4_PRESS_3mm-bleed_cropmarks.pdf"',
                "X-Page-Count": str(pages),
                "X-Variant": "press",
            },
        )
    pdf, pages = await run_in_threadpool(assembler.build_pdf_sync)
    return Response(
        content=pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": 'attachment; filename="Medical_Devices_Complete_Textbook_A4.pdf"',
            "X-Page-Count": str(pages),
        },
    )


app.mount("/api/book/preview/fonts", StaticFiles(directory=str(ROOT_DIR / "book" / "fonts")), name="fonts")
app.mount("/api/book/preview/images", StaticFiles(directory=str(ROOT_DIR / "book" / "images")), name="images")
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def warm_pdf():
    assembler.warm_pdf_async()
