import { useEffect, useState } from "react";
import { SpinnerGap } from "@phosphor-icons/react";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

export default function PreviewPane({ sectionId, sectionLabel }) {
  const [loading, setLoading] = useState(true);
  const [failed, setFailed] = useState(false);

  useEffect(() => {
    setLoading(true);
    setFailed(false);
    const t = setTimeout(() => setLoading(false), 15000); // safety
    return () => clearTimeout(t);
  }, [sectionId]);

  return (
    <div data-testid="preview-pane" className="bg-[#F1F5F9] border border-slate-200 flex flex-col h-full">
      <div className="px-4 py-3 border-b border-slate-200 bg-white flex items-center justify-between">
        <span className="text-[10px] uppercase tracking-[0.2em] font-semibold text-slate-500">Live Typeset Preview</span>
        <span data-testid="preview-section-label" className="text-[11px] font-semibold text-[#0F4C5C]">{sectionLabel}</span>
      </div>
      <div className="flex-1 p-3 relative">
        {loading && !failed && (
          <div data-testid="preview-loading" className="absolute inset-3 bg-white border border-slate-300 flex flex-col items-center justify-center gap-3 z-10">
            <SpinnerGap size={26} className="animate-spin" color="#0F4C5C" />
            <span className="text-[12px] text-slate-500">Rendering A4 preview…</span>
          </div>
        )}
        {failed && (
          <div data-testid="preview-error" className="absolute inset-3 bg-white border border-slate-300 flex flex-col items-center justify-center gap-2 z-10">
            <span className="text-[13px] text-slate-600 font-medium">Preview could not be loaded.</span>
            <button
              className="text-[12px] text-[#0F4C5C] underline"
              onClick={() => { setFailed(false); setLoading(true); }}
            >
              Retry
            </button>
          </div>
        )}
        <iframe
          data-testid="preview-iframe"
          key={sectionId}
          title="A4 preview"
          src={`${BACKEND_URL}/api/book/preview/${sectionId}`}
          className="w-full h-full bg-white border border-slate-300"
          onLoad={() => setLoading(false)}
          onError={() => { setLoading(false); setFailed(true); }}
        />
      </div>
    </div>
  );
}
