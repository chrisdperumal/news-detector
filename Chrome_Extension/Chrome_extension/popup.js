// popup.js

chrome.storage.local.get("title", function(data) {
    document.getElementById("title").textContent = data.title || "No title found.";
  });
  

  // popup.js

// Function to display text based on button click
function displayText(buttonId) {
    var textToShow = "";
    switch(buttonId) {
        case "us":
            textToShow = "US's viewpoint is:";
            break;
        case "europe":
            textToShow = "Europe's viewpoint is";
            break;
        case "india":
            textToShow = "Text for India button.";
            break;
        case "russia":
            textToShow = "Text for Russia button.";
            break;
        case "china":
            textToShow = "Text for China button.";
            break;
        default:
            textToShow = "Unknown button.";
    }
    document.getElementById("textDisplay").textContent = textToShow;
}

// Function to display initial text before any button is clicked
function displayInitialText() {
    document.getElementById("initialText").textContent = "Short summary on what differences can be seen in different countries viewpoints:";
}

// Call the function to display initial text when the page loads
displayInitialText();

// Add event listeners to the buttons
document.getElementById("us").addEventListener("click", function() {
    displayText("us");
});

document.getElementById("europe").addEventListener("click", function() {
    displayText("europe");
});

document.getElementById("india").addEventListener("click", function() {
    displayText("india");
});

document.getElementById("russia").addEventListener("click", function() {
    displayText("russia");
});

document.getElementById("china").addEventListener("click", function() {
    displayText("china");
});
