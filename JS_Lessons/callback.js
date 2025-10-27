// Synchronous callback examples

// Odd number filter
function filter(numbers, callback) {
    let results = [];
    for (const number of numbers) {
        if (callback(number)) {
            results.push(number);
        }
    }
    return results;
}

let numbers = [1, 2, 3, 4, 5, 6, 7];

// Call filter() with isOdd() as an argument
// isOdd is a callback function
let oddNumbers = filter(numbers, (number) => number % 2 !== 0);
console.log(oddNumbers);