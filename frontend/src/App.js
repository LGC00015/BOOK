import { useEffect, useMemo, useState } from "react";
import "@/App.css";
import axios from "axios";
import { toast, Toaster } from "sonner";
import { DownloadSimple, SpinnerGap } from "@phosphor-icons/react";
import Sidebar from "@/components/Sidebar";
import KpiStrip from "@/components/KpiStrip";
import TocPanel from "@/components/TocPanel";
import PreviewPane from "@/components/PreviewPane";
import PhaseTracker from "@/components/PhaseTracker";
import CoverCard from "@/components/CoverCard";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

function App() {
  const [meta, setMeta] = useState(null);
  const [toc, setToc] = useState(null);
  const [selected, setSelected] = useState("ch01");
  const [pdfStatus, setPdfStatus] = useState(null);
  const [downloading, setDownloading] = useState(false);
  const [pendingDownload, setPendingDownload] = useState(false);
  const [activeNav, setActiveNav] = useState("overview");

  useEffect(() => {
    axios.get(`${API}/book/meta`).then((r) => setMeta(r.data)).catch(() => {});
    axios.get(`${API}/book/toc`).then((r) => setToc(r.data)).catch(() => {});
  }, []);

  useEffect(() => {
    let timer;
    const poll = async () => {
      try {
        const r = await axios.get(`${API}/book/pdf/status`);
        setPdfStatus(r.data);
        if (!r.data.ready) timer = setTimeout(poll, 4000);
        else setMeta((m) => (m ? { ...m, pdf: r.data } : m));
      } catch {
        timer = setTimeout(poll, 6000);
      }
    };
    poll();
    return () => clearTimeout(timer);
  }, []);

  const sectionLabel = useMemo(() => {
    if (!toc) return selected;
    const all = [
      ...toc.front_matter,
      ...toc.parts.flatMap((p) => [{ id: `part${p.num}`, title: `Part ${p.num} — ${p.title}` }, ...p.chapters.map((c) => ({ id: c.id, title: `Ch ${c.num} · ${c.title}` }))]),
      ...toc.back_matter,
    ];
    return all.find((s) => s.id === selected)?.title || selected;
  }, [toc, selected]);

  const handleSelect = (id) => {
    setSelected(id);
    setActiveNav("preview");
  };

  const handleNav = (id) => {
    setActiveNav(id);
    const target = id === "overview" ? "section-overview" : id === "contents" ? "section-contents" : "section-preview";
    const el = document.getElementById(target);
    el?.scrollIntoView({ behavior: "smooth", block: id === "overview" ? "end" : "start" });
  };

  const performDownload = async () => {
    setDownloading(true);
    toast.loading("Preparing your A4 PDF…", { id: "pdf" });
    try {
      const r = await axios.get(`${API}/book/pdf`, { responseType: "blob", timeout: 300000 });
      const url = URL.createObjectURL(new Blob([r.data], { type: "application/pdf" }));
      const a = document.createElement("a");
      a.href = url;
      a.download = "Medical_Devices_Complete_Textbook_A4.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
      toast.success(`Downloaded — ${r.headers["x-page-count"] || pdfStatus?.pages || ""} A4 pages typeset.`, { id: "pdf" });
    } catch {
      toast.error("PDF download failed. Please try again.", { id: "pdf" });
    } finally {
      setDownloading(false);
      setPendingDownload(false);
    }
  };

  const downloadPdf = () => {
    if (pdfStatus && !pdfStatus.ready) {
      setPendingDownload(true);
      toast.info("The A4 edition is being typeset — your download will start automatically when it's ready.", { id: "pdf" });
      return;
    }
    performDownload();
  };

  useEffect(() => {
    if (pendingDownload && pdfStatus?.ready && !downloading) {
      performDownload();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [pdfStatus?.ready, pendingDownload]);

  const pdfReady = pdfStatus?.ready;

  return (
    <div className="grain min-h-screen">
      <Toaster position="top-right" richColors />
      <Sidebar meta={meta} active={activeNav} onNav={handleNav} />

      <main className="ml-64 min-h-screen">
        <header className="sticky top-0 z-30 bg-white/95 backdrop-blur border-b border-slate-200 px-8 py-4 flex items-center justify-between">
          <div id="section-overview">
            <div className="text-[10px] uppercase tracking-[0.22em] font-semibold text-[#0F4C5C]">
              {meta?.series || "Core Textbook"}
            </div>
            <h1 className="font-display font-extrabold text-xl tracking-tight text-slate-900">
              {meta ? `${meta.title}: ${meta.subtitle}` : "Loading…"}
            </h1>
          </div>
          <button
            data-testid="pdf-download-btn"
            onClick={downloadPdf}
            disabled={downloading}
            className="flex items-center gap-2 bg-[#0B1121] text-white text-sm font-semibold px-5 py-2.5 border border-[#0B1121] hover:bg-[#0F4C5C] hover:border-[#0F4C5C] transition-colors duration-150 disabled:opacity-60"
          >
            {downloading || (pdfStatus && !pdfReady) ? (
              <SpinnerGap size={17} className="animate-spin" />
            ) : (
              <DownloadSimple size={17} weight="bold" />
            )}
            {downloading
              ? "Downloading…"
              : pdfReady
              ? `Download A4 PDF (${pdfStatus.pages} pp)`
              : pendingDownload
              ? "Typesetting… download queued"
              : "Typesetting… click to queue download"}
          </button>
        </header>

        <div className="p-8 space-y-6">
          <KpiStrip meta={meta} />

          <div id="section-contents" className="grid grid-cols-1 lg:grid-cols-12 gap-6" style={{ minHeight: "640px" }}>
            <div className="lg:col-span-3 rise rise-2"><CoverCard meta={meta} onSelect={handleSelect} /></div>
            <div className="lg:col-span-4 rise rise-3" style={{ maxHeight: "760px" }}>
              <TocPanel toc={toc} selected={selected} onSelect={handleSelect} />
            </div>
            <div id="section-preview" className="lg:col-span-5 rise rise-4" style={{ minHeight: "640px" }}>
              <PreviewPane sectionId={selected} sectionLabel={sectionLabel} />
            </div>
          </div>

          <PhaseTracker phases={meta?.phases} />

          <footer className="text-[11px] text-slate-400 pb-6">
            Typeset with a print-optimized HTML/CSS → WeasyPrint A4 pipeline · 20 chapters, 156 figures & data tables from the author manuscript · Regulatory citations from CDSCO, US FDA, EUR-Lex, ISO, IEC & WHO sources
          </footer>
        </div>
      </main>
    </div>
  );
}

export default App;
