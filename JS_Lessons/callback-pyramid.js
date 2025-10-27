// Nesting callbacks leads to code that is hard to
// read and maintain and is referred to as the
// pyramid of doom.

// This example will demonstrate nested callbacks
// by simulating the fetching of data from a server,
// procesing the data, saving the data and confirming
// all operations were successfully completed.

// The setTimeout() calls simulate the time required to complete
// that task.

// Step 1: Fetch data from server
function fetchDataFromServer(ipAddress, callback) {
    setTimeout(() => {
        const data = { id: 1, name: 'Sample Data' };
        console.log(`Data fetched from the server ${ipAddress}:`, data);
        callback(data);
    }, 1000);   // Timeout for 1 second
}

// Step 2: Process the data
function processServerData(data, callback) {
    setTimeout(() => {
        data.processed = true;
        console.log('Data processed:', data);
        callback(data);
    }, 1000);   // Timeout for 1 second
}

// Step 3: Save the data to server
function saveDataToServer(data, callback) {
    setTimeout(() => {
        const date = new Date();
        data.lastSaved = date;  // Add 'last saved' property to object
        console.log('Saved to server:', data);
        callback(data);
    }, 1000);   // Timeout for 1 second
}

// Step 4: Confirmation sent to client
function sendConfirmationToClient(data, callback) {
    setTimeout(() => {
        data.clientConfirmation = true;
        console.log('Confirmation sent:', data);
        callback(data);
    }, 1000);   // Timeout for 1 second
}

const serverAddress = '114.102.9.1';

fetchDataFromServer(serverAddress, (data) => {
    processServerData(data, (processedData) => {
        saveDataToServer(processedData, (savedData) => {
            sendConfirmationToClient(savedData, (confirmationData) => {
                console.log('All operations complete.', confirmationData);
            });
        });
    });
});