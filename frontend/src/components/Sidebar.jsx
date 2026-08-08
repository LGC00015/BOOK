import { Books, SquaresFour, ListNumbers, Eye, CircleDashed, CheckCircle } from "@phosphor-icons/react";

const NAV = [
  { id: "overview", label: "Overview", icon: SquaresFour },
  { id: "contents", label: "Contents", icon: ListNumbers },
  { id: "preview", label: "Live Preview", icon: Eye },
];

export default function Sidebar({ meta, active, onNav }) {
  const phases = meta?.phases || [];
  return (
    <aside data-testid="sidebar" className="w-64 fixed left-0 top-0 h-full border-r border-slate-200 bg-white flex flex-col z-40">
      <div className="px-6 py-6 border-b border-slate-200">
        <div className="flex items-center gap-2.5">
          <div className="w-9 h-9 bg-[#0F4C5C] flex items-center justify-center">
            <Books size={20} weight="duotone" color="#fff" />
          </div>
          <div>
            <div className="font-display font-extrabold text-[15px] leading-tight tracking-tight">MD PRESS</div>
            <div className="text-[10px] uppercase tracking-[0.18em] text-slate-500">Book Production</div>
          </div>
        </div>
      </div>

      <nav className="px-3 py-4">
        {NAV.map((n) => {
          const Icon = n.icon;
          const isActive = active === n.id;
          return (
            <button
              key={n.id}
              data-testid={`nav-${n.id}`}
              onClick={() => onNav(n.id)}
              className={`w-full flex items-center gap-3 px-3 py-2.5 text-sm mb-0.5 border transition-colors duration-150 ${
                isActive
                  ? "bg-[#0B1121] text-white border-[#0B1121]"
                  : "text-slate-600 border-transparent hover:bg-slate-100 hover:text-slate-900"
              }`}
            >
              <Icon size={17} weight={isActive ? "fill" : "regular"} />
              {n.label}
            </button>
          );
        })}
      </nav>

      <div className="px-6 pt-4 pb-2 text-[10px] uppercase tracking-[0.2em] font-semibold text-slate-400">
        Production Phases
      </div>
      <div className="px-6 flex-1 overflow-y-auto">
        {phases.map((p) => (
          <div key={p.num} data-testid={`sidebar-phase-${p.num}`} className="flex items-start gap-2.5 py-2 border-b border-slate-100 last:border-0">
            {p.status === "complete" ? (
              <CheckCircle size={15} weight="fill" color="#059669" className="mt-0.5 shrink-0" />
            ) : (
              <CircleDashed size={15} color="#94A3B8" className="mt-0.5 shrink-0" />
            )}
            <div>
              <div className={`text-[12px] leading-snug ${p.status === "complete" ? "text-slate-800" : "text-slate-400"}`}>
                <span className="font-semibold">P{p.num}.</span> {p.title}
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="px-6 py-4 border-t border-slate-200 text-[11px] text-slate-400 leading-relaxed">
        {meta?.syllabus_anchor || "PCI NEP 2020 · BP708T"}
      </div>
    </aside>
  );
}
