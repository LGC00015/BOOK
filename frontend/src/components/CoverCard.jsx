export default function CoverCard({ meta, onSelect }) {
  return (
    <div data-testid="cover-card" className="bg-white border border-slate-200 flex flex-col h-full">
      <div className="px-4 py-3 border-b border-slate-200">
        <span className="text-[10px] uppercase tracking-[0.2em] font-semibold text-slate-500">Book Cover</span>
      </div>
      <div className="p-4 flex-1 flex flex-col">
        <button
          data-testid="cover-thumb"
          onClick={() => onSelect("cover")}
          className="a4-frame w-full bg-[#093542] relative overflow-hidden text-left group border border-[#093542]"
        >
          <div className="absolute inset-0 opacity-20"
            style={{ backgroundImage: "linear-gradient(#0F4C5C 1px, transparent 1px), linear-gradient(90deg, #0F4C5C 1px, transparent 1px)", backgroundSize: "26px 26px" }} />
          <div className="relative p-5 flex flex-col h-full">
            <span className="text-[8px] uppercase tracking-[0.3em] text-[#7FB6C4] border border-[#2C6B7C] px-2 py-1 self-start">
              Core Textbook
            </span>
            <div className="font-display font-extrabold text-white text-2xl leading-tight mt-6">
              MEDICAL<br />DEVICES<span className="text-[#8FD6E8]">.</span>
            </div>
            <div className="text-[10px] text-[#BCD9E1] mt-3 leading-relaxed" style={{ fontFamily: "Spectral, serif", fontStyle: "italic" }}>
              A Comprehensive Textbook for Pharmacy and Allied Health Sciences
            </div>
            <div className="mt-auto pt-4 border-t border-[#2C6B7C]">
              <div className="text-[10px] font-bold text-white">{meta?.author || "Author Name"}</div>
              <div className="text-[8.5px] text-[#7FB6C4] mt-0.5">{meta?.publisher} · {meta?.year}</div>
            </div>
          </div>
          <div className="absolute inset-0 bg-white opacity-0 group-hover:opacity-5 transition-opacity duration-200" />
        </button>
        <div className="mt-4 space-y-1.5 text-[11.5px]">
          <div className="flex justify-between"><span className="text-slate-400">Edition</span><span className="text-slate-700 font-medium">{meta?.edition}</span></div>
          <div className="flex justify-between"><span className="text-slate-400">Format</span><span className="text-slate-700 font-medium">A4 · Full color · Print-ready</span></div>
          <div className="flex justify-between"><span className="text-slate-400">ISBN</span><span className="text-slate-700 font-medium">Ready for assignment</span></div>
          <div className="flex justify-between"><span className="text-slate-400">Syllabus</span><span className="text-slate-700 font-medium">B.Pharm Elective</span></div>
        </div>
      </div>
    </div>
  );
}
