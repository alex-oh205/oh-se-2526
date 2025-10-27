function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const data = { id: 1, name: "Andrei" };
            // const data = "";
            if (data) {
                resolve(data);
            } else {
                reject("Andrei is not found");
            }
        }, 1000);
    });
}

fetchData()
    .then(data => {
        console.log('Data:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });