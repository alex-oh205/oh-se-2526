// Returns a Promise that resolves two seconds after calling
// and prints out 'Hello World' to console
function greeting() {
    return new Promise(resolve => {
        setTimeout(() => {
            console.log('Hello World');
            resolve();
        }, 2000);   // Wait two seconds
    });
}

greeting();