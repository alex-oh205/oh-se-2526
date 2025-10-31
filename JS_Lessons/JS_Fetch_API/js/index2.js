/* Use JS to fetch image data and convert it to an image element using
   async and await. Async and await can be used to condense the .then
   code from the previous example and make it more readable
   
   -- "Async" keyword defines a function as asynchronous
   -- "Async" function will always return a promise.
   -- "Await" keyword can only be used inside an "async" function
   -- When "Await" keyword is reached, the execution of the async function
      is paused until the promise it's "awaiting" is resolved or rejected.
   -- If the promise is resolved, "await" evaluates the resolved value and the
      async function continues to execute.
   -- If the promise is rejected, "await" returns the error (rejected value) */

const imageUrl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc9APxkj0xClmrU3PpMZglHQkx446nQPG6lA&s";
console.log('Fetching the image.');

async function getImage(url) {
    // Await the result of fetch and store it in the variable response
    const response = await fetch(url);
    const blob = await response.blob();

    // Convert BLOB to proper HTML image URL
    document.getElementById('image').src = URL.createObjectURL(blob);
}

getImage(imageUrl)
    .then(resolve => {
        console.log('Image loaded.');
    })
    .catch(reject => {
        console.log('Image could not be loaded.');
        console.error(reject);
    });