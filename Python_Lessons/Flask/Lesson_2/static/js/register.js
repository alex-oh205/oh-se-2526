// This JS file is for registering a new app user ---------------------------//

// ----------------- Firebase Setup & Initialization ------------------------//
// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.6.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword }
  from "https://www.gstatic.com/firebasejs/12.6.0/firebase-auth.js";

import { getDatabase, ref, set, update, child, get }
  from "https://www.gstatic.com/firebasejs/12.6.0/firebase-database.js"

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCulWp7R1ke0zzPtKY7DKCpKASAoSPkIz4",
  authDomain: "se-321-2526-firebase-dem-fcdc8.firebaseapp.com",
  databaseURL: "https://se-321-2526-firebase-dem-fcdc8-default-rtdb.firebaseio.com",
  projectId: "se-321-2526-firebase-dem-fcdc8",
  storageBucket: "se-321-2526-firebase-dem-fcdc8.firebasestorage.app",
  messagingSenderId: "898314766040",
  appId: "1:898314766040:web:7f6c681525b6f5368179ad"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase Authentication
const auth = getAuth();

// Return instance of your app's Firebase Realtime Database (FRD)
const db = getDatabase();

// ---------------- Register New User --------------------------------//

document.getElementById("submitData").onclick = function() {
  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const email = document.getElementById("userEmail").value;

  // Firebase will require a password of at least 6 characters
  const password = document.getElementById("userPass").value;

  // Validate user inputs
  if (!validation(firstName, lastName, email, password)) {
    return;
  }

  createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // User account created and signed in successfully
    const user = userCredential.user;
    
    // Add user account info to realtime database
    // 'set' will create a new reference or completely replace an existing one
    set(ref(db, 'users/' + user.uid + '/accountInfo'), {
      uid: user.uid,  // Save the userID for home.js reference
      email: email,
      firstname: firstName,
      lastname: lastName
    })
    .then(() => {
      alert('User created successfully!') // Alert for successful creation
    })
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert(errorMessage);
  });
}

// --------------- Check for null, empty ("") or all spaces only ------------//
function isEmptyorSpaces(str){
  return str === null || str.match(/^ *$/) !== null
}

// ---------------------- Validate Registration Data -----------------------//
function validation(firstName, lastName, email, password) {
  let fNameRegex = /^[a-zA-Z]+$/;
  let lNameRegex = /^[a-zA-Z]+$/;
  let emailRegex = /^[a-zA-Z0-9]+@ctemc\.org$/;

  if (isEmptyorSpaces(firstName) || isEmptyorSpaces(lastName) ||
      isEmptyorSpaces(email) || isEmptyorSpaces(password)) {
    alert("Please complete all fields.");
    return false;
  }

  if (!fNameRegex.test(firstName)) {
    alert("The first name should only contain letters.");
    console.log(fNameRegex);
    return false;
  }

  if (!lNameRegex.test(lastName)) {
    alert("The last name should only contain letters.");
    console.log(lNameRegex);
    return false;
  }

  if (!emailRegex.test(email)) {
    alert("Please enter a valid email.");
    console.log(emailRegex);
    return false;
  }

  return true;
}