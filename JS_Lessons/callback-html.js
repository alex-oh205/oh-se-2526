// Use JS callback function within a webpage

// Prompt for username
function getUserName(callback) {
    const userName = prompt("Enter your name:");
    callback(userName);
}

// Define the callback function: greeting
function greeting(name) {
    document.getElementById("greeting").innerHTML = 
    `<h1>Hello ${name}!</h1>`;
}

getUserName(greeting);