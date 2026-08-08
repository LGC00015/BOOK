import { CheckCircle, CircleDashed } from "@phosphor-icons/react";

export default function PhaseTracker({ phases }) {
  if (!phases?.length) return null;
  return (
    <div data-testid="phase-tracker" className="bg-white border border-slate-200 p-6">
      <div className="text-[10px] uppercase tracking-[0.2em] font-semibold text-slate-500 mb-5">
        Production Pipeline — 6 Phases
      </div>
      <div className="grid grid-cols-2 lg:grid-cols-6 gap-0 border border-slate-200">
        {phases.map((p, i) => (
          <div
            key={p.num}
            data-testid={`phase-step-${p.num}`}
            className={`p-4 ${i !== phases.length - 1 ? "border-r border-slate-200" : ""} ${
              p.status === "complete" ? "bg-[#F0F7F8]" : "bg-white"
            }`}
          >
            <div className="flex items-center gap-2">
              {p.status === "complete" ? (
                <CheckCircle size={16} weight="fill" color="#0F4C5C" />
              ) : (
                <CircleDashed size={16} color="#94A3B8" />
              )}
              <span className={`font-display font-bold text-sm ${p.status === "complete" ? "text-[#0F4C5C]" : "text-slate-400"}`}>
                Phase {p.num}
              </span>
            </div>
            <div className={`text-[12px] mt-2 leading-snug ${p.status === "complete" ? "text-slate-800" : "text-slate-500"}`}>
              {p.title}
            </div>
            <div className="text-[10.5px] text-slate-400 mt-1 leading-snug">{p.detail}</div>
            <div
              className={`mt-3 text-[9px] uppercase tracking-[0.12em] font-semibold inline-block px-1.5 py-0.5 border ${
                p.status === "complete"
                  ? "bg-[#ECFDF5] text-[#059669] border-[#A7F3D0]"
                  : "bg-[#FFFBEB] text-[#D97706] border-[#FDE68A]"
              }`}
            >
              {p.status === "complete" ? "Complete" : "Queued"}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
