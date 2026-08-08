const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

export default function PreviewPane({ sectionId, sectionLabel }) {
  return (
    <div data-testid="preview-pane" className="bg-[#F1F5F9] border border-slate-200 flex flex-col h-full">
      <div className="px-4 py-3 border-b border-slate-200 bg-white flex items-center justify-between">
        <span className="text-[10px] uppercase tracking-[0.2em] font-semibold text-slate-500">Live Typeset Preview</span>
        <span data-testid="preview-section-label" className="text-[11px] font-semibold text-[#0F4C5C]">{sectionLabel}</span>
      </div>
      <div className="flex-1 p-3">
        <iframe
          data-testid="preview-iframe"
          key={sectionId}
          title="A4 preview"
          src={`${BACKEND_URL}/api/book/preview/${sectionId}`}
          className="w-full h-full bg-white border border-slate-300"
        />
      </div>
    </div>
  );
}
