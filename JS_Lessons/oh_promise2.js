// Returns a Promise resolving if data is odd and
// rejecting if data is not a number or is even.
const value = (data) => {
    return new Promise((resolve, reject) => {
        if (isNaN(data)) {                  // Checks if data is not a number
            reject("Error. Not a number.");
        } else if (data % 2 === 0) {        // Checks if data is even
            reject("even");
        } else if (data % 2 === 1) {        // Checks if data is odd
            resolve("odd");
        }
    });
}

value(2)
    .then(resolved => {
        console.log(resolved);
    })
    .catch(rejected => {
        console.log("Error:", rejected);
    });