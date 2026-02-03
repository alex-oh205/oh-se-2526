/*
Name: Alex Oh
File: oh_regex.js
Objective: Use regular expressions to validate user input for first name, last name, and email address.
*/

// Values for testing
let firstName = "Alex";
let lastName = "Oh";
let email = "aloh@ctemc.org";

const isEmptyOrSpaces = (str) => {
    // Check if the string is null or contains only spaces
    return str === null || str.match(/^ *$/) !== null;
};

const validation = (firstName, lastName, email) => {
    // Checks for valid first name, last name, and email using regex

    let firstNameRegex = /^[a-zA-Z]+$/; // Checks for letters only
    let lastNameRegex = /^[a-zA-Z]+$/;  // Checks for letters only
    let emailRegex = /^[a-zA-Z0-9]+@(ctemc|gmail|yahoo).(org|com|edu)$/; // Checks for valid email format

    // Check for empty fields
    if (isEmptyOrSpaces(firstName) || isEmptyOrSpaces(lastName) || isEmptyOrSpaces(email)) {
        console.log("Please complete all fields.");
        return false;
    }

    // Validate first name
    if (!firstNameRegex.test(firstName)) {
        console.log("The first name should only contain letters.");
        return false;
    }

    // Validate last name
    if (!lastNameRegex.test(lastName)) {
        console.log("The last name should only contain letters.");
        return false;
    }

    // Validate email
    if (!emailRegex.test(email)) {
        console.log("The email address is not valid.");
        return false;
    }

    console.log("All inputs have been validated!");
    return true;
}

validation(firstName, lastName, email);