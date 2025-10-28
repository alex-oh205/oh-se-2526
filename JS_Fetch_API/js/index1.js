/* Use JS to fetch image data and convert it to an image element using
    .then method */

const imageUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc9APxkj0xClmrU3PpMZglHQkx446nQPG6lA&s";
console.log('Fetching the image.');

fetch(imageUrl) // Fetch the image, which is returned in the response as a BLOB
                // Ignore the metadata.
                // All of the producing code is abstracted. We need to build the consuming code.
.then(response => {
    console.log(response);
    return response.blob();
}).then(blob => {
    // Convert BLOB to proper HTML image URL
    document.getElementById('image').src = URL.createObjectURL(blob);
    console.log('Here is the BLOB: ', URL.createObjectURL(blob));
}).catch(error => {
    console.error('Error. Image could not be loaded.');
    console.error(error);
});