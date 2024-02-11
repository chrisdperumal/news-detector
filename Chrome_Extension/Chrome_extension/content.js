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
      fetchHotWordsfromTitle(title); // Call fetchHotWordsfromTitle with the title
    })
    .catch(error => {
      console.error("Error fetching title:", error);
      chrome.runtime.sendMessage({ message: "show_error", error: error });
    });
}

function fetchHotWordsfromTitle(title) {
  // Implement the function to extract hot words from the title
  // You can use the provided Python code translated to JavaScript
  
  const result = [];
  const posTag = ['PROPN', 'ADJ', 'NOUN'];
  const doc = nlp(title.toLowerCase()); // Assuming nlp is defined
  for (const token of doc) {
      if (nlp.Defaults.stopWords.includes(token.text) || punctuation.includes(token.text)) {
          continue;
      }
      if (posTag.includes(token.pos_)) {
          result.push(token.text);
      }
  }
  
  // Display hot words or do any further processing here
  console.log(result);
}
