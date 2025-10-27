// Daisy chaining promises
// Order of events: clean room, take garbage out, get ice cream

let cleanRoom = () => {
    return new Promise((resolve, reject) => {
        let roomCleaned = true;

        if (roomCleaned) {
            resolve('Cleaned the room.\n');
        } else {
            reject('Room not clean.');
        }
    });
};

let garbageOut = (message) => {
    return new Promise((resolve, reject) => {
        let tookOutGarbage = true;

        if (tookOutGarbage) {
            resolve(message + 'Took out the garbage.\n');
        } else {
            reject(message + "However, the garbage wasn't taken out.");
        }
    });
};

let getIceCream = (message) => {
    return new Promise((resolve, reject) => {
        resolve(message + 'Got ice cream.\n');
    });
};

let homework = (message) => {
    return new Promise((resolve, reject) => {
        let finishedHomework = true;

        if (finishedHomework) {
            resolve(message + "Finished homework.");
        } else {
            reject(message + "Didn't finish homework.");
        }
    });
}

cleanRoom().then(fromCleanResolve => {
    return garbageOut(fromCleanResolve);
}).then(fromGarbageResolve => {
    return getIceCream(fromGarbageResolve);
}).then(fromIceCream => {
    return homework(fromIceCream);
}).then(fromHomeworkResolve => {
    console.log(fromHomeworkResolve);
}).catch(fromReject => {
    console.log(fromReject);
})