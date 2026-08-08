export default function TocPanel({ toc, selected, onSelect }) {
  if (!toc) return <div className="bg-white border border-slate-200 p-6 text-sm text-slate-400">Loading contents…</div>;

  const Row = ({ id, label, num, status }) => (
    <button
      data-testid={`toc-row-${id}`}
      onClick={() => onSelect(id)}
      className={`row-hover w-full flex items-center gap-3 px-4 py-2 text-left border-l-2 ${
        selected === id ? "border-[#0F4C5C] bg-[#F0F7F8]" : "border-transparent"
      }`}
    >
      {num !== undefined && (
        <span className="font-display font-bold text-[13px] text-slate-400 w-6 shrink-0">{String(num).padStart(2, "0")}</span>
      )}
      <span className="text-[13px] text-slate-800 flex-1 leading-snug">{label}</span>
      {status && (
        <span
          data-testid={`chapter-status-badge-${id}`}
          className={`text-[9px] uppercase tracking-[0.1em] font-semibold px-1.5 py-0.5 border shrink-0 ${
            status === "complete"
              ? "bg-[#ECFDF5] text-[#059669] border-[#A7F3D0]"
              : "bg-[#FFFBEB] text-[#D97706] border-[#FDE68A]"
          }`}
        >
          {status === "complete" ? "Complete" : "In Dev"}
        </span>
      )}
    </button>
  );

  return (
    <div data-testid="toc-panel" className="bg-white border border-slate-200 flex flex-col h-full">
      <div className="px-4 py-3 border-b border-slate-200 flex items-center justify-between">
        <span className="text-[10px] uppercase tracking-[0.2em] font-semibold text-slate-500">Table of Contents</span>
        <span className="text-[11px] text-slate-400">click to preview</span>
      </div>
      <div className="overflow-y-auto flex-1 py-2">
        <div className="px-4 pt-1 pb-1 text-[10px] uppercase tracking-[0.16em] font-semibold text-[#0F4C5C]">Front Matter</div>
        {toc.front_matter.map((f) => (
          <Row key={f.id} id={f.id} label={f.title} />
        ))}
        {toc.parts.map((p) => (
          <div key={p.num}>
            <div className="px-4 pt-3 pb-1 text-[10px] uppercase tracking-[0.16em] font-semibold text-[#0F4C5C]">
              Part {p.num} — {p.title}
            </div>
            <Row id={`part${p.num}`} label="Part divider" />
            {p.chapters.map((c) => (
              <Row key={c.id} id={c.id} num={c.num} label={c.title} status={c.status === "complete" ? "complete" : "planned"} />
            ))}
          </div>
        ))}
        <div className="px-4 pt-3 pb-1 text-[10px] uppercase tracking-[0.16em] font-semibold text-[#0F4C5C]">Back Matter</div>
        {toc.back_matter.map((b) => (
          <Row key={b.id} id={b.id} label={b.title} />
        ))}
      </div>
    </div>
  );
}
