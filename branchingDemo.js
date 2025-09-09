const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

// getMonth() returns the month as an integer (0 - 11). Jan = 0, Dec = 11
const d = new Date();
let month = months[d.getMonth()];

console.log("The month is: " + month);