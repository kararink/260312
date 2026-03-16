// context menu ID
const CONTEXT_MENU_ID = "save-image-as-png";

// Create the context menu on install
chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: CONTEXT_MENU_ID,
    title: "PNGとして保存",
    contexts: ["image"]
  });
});

// Helper function to manage the offscreen document
let creating; // A global promise to avoid concurrency issues
async function setupOffscreenDocument(path) {
  // Check all windows controlled by the service worker to see if one 
  // of them is the offscreen document with the given path
  const offscreenUrl = chrome.runtime.getURL(path);
  const existingContexts = await chrome.runtime.getContexts({
    contextTypes: ['OFFSCREEN_DOCUMENT'],
    documentUrls: [offscreenUrl]
  });

  if (existingContexts.length > 0) {
    return;
  }

  // create offscreen document
  if (creating) {
    await creating;
  } else {
    creating = chrome.offscreen.createDocument({
      url: path,
      reasons: ['DOM_PARSER', 'BLOBS'], // BLOBS for canvas processing
      justification: 'Convert image format via canvas',
    });
    await creating;
    creating = null;
  }
}

// Listen for clicks on the context menu
chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId === CONTEXT_MENU_ID) {
    const imageUrl = info.srcUrl;
    
    if (!imageUrl) {
        console.error("No image URL found.");
        return;
    }

    try {
      await setupOffscreenDocument('offscreen.html');

      // Send the image URL to the offscreen document to convert
      const dataUrl = await chrome.runtime.sendMessage({
        target: 'offscreen',
        action: 'convertImageToPng',
        data: imageUrl
      });

      if (dataUrl) {
          // Extract filename from original URL, or use a default one
          let filename = "downloaded_image.png";
          try {
             // Basic attempt to get a logical name
             const urlObj = new URL(imageUrl);
             let pathname = urlObj.pathname.split('/').pop();
             if (pathname) {
                 // replace invalid characters and extensions
                 pathname = pathname.replace(/[<>:"/\\|?*]/g, '_');
                 pathname = pathname.replace(/\.[^/.]+$/, ""); // remove old extension
                 if(pathname.length > 0) {
                     filename = pathname + ".png";
                 }
             }
          } catch(e) {
              console.log("Could not parse url for filename, using default", e);
          }
          
          chrome.downloads.download({
              url: dataUrl,
              filename: filename,
              saveAs: true // prompt the user to save
          });
      } else {
          console.error("Failed to convert image to PNG: No dataURL returned.");
      }
    } catch (e) {
      console.error("Error creating offscreen document or converting image:", e);
    }
  }
});
