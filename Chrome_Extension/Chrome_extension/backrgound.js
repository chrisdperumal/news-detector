// Listen for clicks on the extension icon
chrome.action.onClicked.addListener(async (tab) => {
    // Get the current active tab
    let [activeTab] = await chrome.tabs.query({ active: true, currentWindow: true });
  
    // Extract the URL of the active tab
    let url = activeTab.url;
  
    // Log or use the URL as needed
    console.log("Current URL:", url);
  });
  