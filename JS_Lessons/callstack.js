// Callstack example

function first() {
    second();
    console.log("first executed");
}

function second() {
    third();
    console.log("second executed");
}

function third() {
    console.log("third executed");
}

first();
