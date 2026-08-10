import { FileText, BookOpen, ChartBar, Table } from "@phosphor-icons/react";

export default function KpiStrip({ meta }) {
  const pages = meta?.pdf?.pages || 0;
  const kpis = [
    { id: "pages", label: "Typeset A4 Pages", value: pages ? pages : "…", sub: pages ? "compiled edition" : "typesetting", icon: FileText },
    { id: "chapters", label: "Chapters Typeset", value: `${meta?.chapters_complete ?? 0}/${meta?.chapters_total ?? 20}`, sub: "complete edition", icon: BookOpen },
    { id: "figures", label: "Figures", value: meta?.figures_count ?? 0, sub: "numbered & captioned", icon: ChartBar },
    { id: "tables", label: "Tables", value: meta?.tables_count ?? 0, sub: "comparison & data", icon: Table },
  ];
  return (
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
      {kpis.map((k, i) => {
        const Icon = k.icon;
        return (
          <div key={k.id} data-testid={`kpi-${k.id}`} className={`kpi-card bg-white border border-slate-200 p-5 rise rise-${i + 1}`}>
            <div className="flex items-center justify-between">
              <span className="text-[10px] uppercase tracking-[0.18em] font-semibold text-slate-500">{k.label}</span>
              <Icon size={18} weight="duotone" color="#0F4C5C" />
            </div>
            <div className="font-display font-extrabold text-3xl mt-3 tracking-tight text-slate-900">{k.value}</div>
            <div className="text-[11px] text-slate-400 mt-1">{k.sub}</div>
          </div>
        );
      })}
    </div>
  );
}
