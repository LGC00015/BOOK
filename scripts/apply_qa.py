"""Apply the QA corrections layer to the extracted chapter JSONs.

Run:  python3 /app/scripts/apply_qa.py
Idempotent: re-running after re-extraction re-applies the corrections.
Validates that every file remains parseable JSON after substitution.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, "/app/backend")
from book.qa_corrections import CORRECTIONS  # noqa: E402

CONTENT = Path("/app/backend/book/content")


def main():
    total_applied = 0
    total_missed = []
    for ch_id, pairs in sorted(CORRECTIONS.items()):
        f = CONTENT / (ch_id + ".json")
        txt = f.read_text(encoding="utf-8")
        applied = 0
        for find, repl in pairs:
            if repl in txt and find not in txt:
                continue  # already applied
            n = txt.count(find)
            if n == 0:
                total_missed.append((ch_id, find[:70]))
                continue
            txt = txt.replace(find, repl)
            applied += n
        json.loads(txt)  # must still be valid JSON
        f.write_text(txt, encoding="utf-8")
        total_applied += applied
        print(f"{ch_id}: {applied} substitution(s)")
    print(f"\nTOTAL applied: {total_applied}")
    if total_missed:
        print("NOT FOUND (already applied or wording changed):")
        for ch_id, s in total_missed:
            print(f"  {ch_id}: {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
