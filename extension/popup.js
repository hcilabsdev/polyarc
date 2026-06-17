const DEFAULT_API = "http://localhost:8088";
const api = document.getElementById("api");
const ok = document.getElementById("ok");
chrome.storage.sync.get({ apiBase: DEFAULT_API }, (d) => { api.value = d.apiBase; });
document.getElementById("save").onclick = () => {
  const v = (api.value || DEFAULT_API).replace(/\/+$/, "");
  chrome.storage.sync.set({ apiBase: v }, () => {
    ok.textContent = "Saved ✓"; setTimeout(() => (ok.textContent = ""), 1500);
  });
};
