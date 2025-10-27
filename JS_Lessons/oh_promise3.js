// This example will demonstrate the use of Promises to
// simulate the fetching of data from a server,
// processing the data, saving the data and confirming
// all operations were successfully completed.

// The setTimeout() calls simulate the time required to complete
// that task.

// Step 1: Fetch data from server
function fetchDataFromServer(ipAddress) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = { id: 1, name: 'Sample Data' };
            // const data = "";
            if (data) {
                console.log(`Data fetched from the server ${ipAddress}:`, data);
                resolve(data);
            } else {
                reject('Data not found');
            }
        }, 1000);   // Timeout for 1 second
    });
}

// Step 2: Process the data
function processServerData(data) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            data.processed = true;
            // data.processed = false;
            if (data.processed) {
                console.log('Data processed:', data);
                resolve(data);
            } else {
                reject('Data processing failed');
            }
        }, 1000);   // Timeout for 1 second
    });
}

// Step 3: Save the data to server
function saveDataToServer(data) {
    return new Promise(resolve => {
        setTimeout(() => {
            const date = new Date();
            data.lastSaved = date;  // Add 'last saved' property to object
            console.log('Saved to server:', data);
            resolve(data);
        }, 1000);   // Timeout for 1 second
    });
}

// Step 4: Confirmation sent to client
function sendConfirmationToClient(data) {
    return new Promise(resolve => {
        setTimeout(() => {
            data.clientConfirmation = true;
            console.log('Confirmation sent:', data);
            resolve(data);
        }, 1000);   // Timeout for 1 second
    });
}

const serverAddress = '114.102.9.1';

fetchDataFromServer(serverAddress)
    .then(data => {
        return processServerData(data);
    })
    .then(processedData => {
        return saveDataToServer(processedData);
    })
    .then(savedData => {
        return sendConfirmationToClient(savedData);
    })
    .then(confirmationData => {
        console.log('All operations complete.', confirmationData);
    })
    .catch(error => {
        console.log("Error:", error);
    });