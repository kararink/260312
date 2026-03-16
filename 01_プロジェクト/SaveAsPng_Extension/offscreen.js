// Listen for messages from the service worker
chrome.runtime.onMessage.addListener(handleMessages);

async function handleMessages(message, sender, sendResponse) {
  // Only handle targeted messages
  if (message.target !== 'offscreen') return false;

  if (message.action === 'convertImageToPng') {
    // Keep the message channel open for the async response
    convertImageToPng(message.data)
        .then(dataUrl => sendResponse(dataUrl))
        .catch(err => {
            console.error("Conversion error:", err);
            sendResponse(null);
        });
    return true; // Indicates we will send a response asynchronously
  }
}

async function convertImageToPng(imageUrl) {
    try {
        // Fetch the image data
        const response = await fetch(imageUrl);
        const blob = await response.blob();
        
        // Create an ImageBitmap from the blob
        const imageBitmap = await createImageBitmap(blob);
        
        // Create an offscreen canvas
        const canvas = new OffscreenCanvas(imageBitmap.width, imageBitmap.height);
        const ctx = canvas.getContext('2d');
        
        // Draw the image onto the canvas
        ctx.drawImage(imageBitmap, 0, 0);
        
        // We need a FileReader to convert the Blob back to a Data URL
        // because OffscreenCanvas doesn't have a direct toDataURL method
        const convertedBlob = await canvas.convertToBlob({ type: 'image/png' });
        
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onloadend = () => resolve(reader.result);
            reader.onerror = reject;
            reader.readAsDataURL(convertedBlob);
        });
        
    } catch (error) {
        console.error("Error details:", error);
        throw error;
    }
}
