// Function to fetch keywords from the title
function fetchKeywords(title) {
    if (title) {
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
        // Display hot words in the HTML
        document.getElementById("hotwords").textContent = result.join(", ");
    }
}

// Retrieve and display title
chrome.storage.local.get("title", function(data) {
    const titleElement = document.getElementById("title");
    const title = data.title || "No title found.";
    titleElement.textContent = title;
    // Call fetchKeywords function with the title
    fetchKeywords(title);
});

// Function to display text based on button click
function displayText(buttonId) {
    var textToShow = "";
    switch(buttonId) {
        case "United States":
            textToShow = "US's viewpoint is:";
            break;
        case "Germany":
            textToShow = "Europe's viewpoint is";
            break;
        case "India":
            textToShow = "Text for India button.";
            break;
        case "Russia":
            textToShow = "Text for Russia button.";
            break;
        case "China":
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
document.getElementById("United States").addEventListener("click", function() {
    displayText("United States");
});

document.getElementById("Germany").addEventListener("click", function() {
    displayText("Germany");
});

document.getElementById("India").addEventListener("click", function() {
    displayText("India");
});

document.getElementById("Russia").addEventListener("click", function() {
    displayText("Russia");
});

document.getElementById("China").addEventListener("click", function() {
    displayText("China");
});
