// Define promise
// Promise takes 1 function parameter, which itself takes 2 methods: resolve & reject
let promiseToCleanRoom = new Promise((resolve, reject) => {
    // Part 1: What promise must do (may take some time - done asynchronously)
    // Cleaning room

    let isClean = true;        // Is room clean?

    // Part 2: Fulfill promise by resolving or rejecting it
    if (isClean) {
        resolve('clean');
    } else {
        reject('not clean');
    }
});

// Part 3: Call .then() or .catch() when promise is settled
promiseToCleanRoom.then((fromResolve) => {
    console.log(`The room is ${fromResolve}.`);
}).catch((fromReject) => {
    console.log(`The room is ${fromReject}.`);
});