// content.js

chrome.runtime.sendMessage({ message: "get_url" }, function(response) {
    if (response && response.url) {
      fetchTitle(response.url);
    }
  });

function fetchTitle(url) {
  fetch(url)
    .then(response => response.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");
      const title = doc.querySelector("title").innerText;
      chrome.runtime.sendMessage({ message: "show_title", title: title });
    })
    .catch(error => {
      console.error("Error fetching title:", error);
      chrome.runtime.sendMessage({ message: "show_error", error: error });
    });
}


