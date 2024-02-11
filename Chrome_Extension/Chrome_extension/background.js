// background.js

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.message === "get_url") {
    sendResponse({ url: sender.tab.url });
  } else if (request.message === "show_title") {
    chrome.storage.local.set({ title: request.title });
  }
});
