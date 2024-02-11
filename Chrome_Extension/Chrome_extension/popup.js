// popup.js

chrome.storage.local.get("title", function(data) {
    document.getElementById("title").textContent = data.title || "No title found.";
  });
  