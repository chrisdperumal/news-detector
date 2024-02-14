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

  
}

function getSummaryFromKeywords(keywords){
  fetch('http://localhost:3000/v1/keywords', {
    method: 'POST', // Specify the method
    headers: {
      'Content-Type': 'application/json', // Specify the content type
    },
    body: JSON.stringify({
      key: JSON.stringify(keywords), // Your data goes here
    }),
  })
  .then(response => response.json()) // Parse the response as JSON
  .then(data => {
    console.log(data); // Handle the data from the API
  })
  .catch(error => {
      console.error('Error:', error); // Handle any errors
  });
  
}
