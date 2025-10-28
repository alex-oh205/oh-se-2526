/*
    This script file demonstrates how to split and slice the CSV data
    Data from: https://data.giss.nasa.gov/gistemp/ (Zonal annual means 1880-pres)
    Values are temperature differences from the mean of 14 deg-C.
    Mean from: https://earthobservatory.nasa.gov/world-of-change/global-temperatures
*/


async function getData() {
    const response = await fetch('../data/test.csv');   // .. to move up one folder
    const data = await response.text();                 // CSV to TEXT format

    // \n - new line character
    // split('\n') - will separate the table into an array of individual rows
    // slice(start, end) - return a new array starting at index "start" up and including "end"
    const table = data.split('\n').slice(1);    // Split by line and remove first row
    console.log(table);

    table.forEach(row => {
        const columns = row.split(',');
        const year = columns[0];    // assign year value (type: string)
        const temp = columns[1];    // assign global temp. deviation value (string)
        const nhTemp = columns[2];  // assign north. hem. temp. (string)
        const shTemp = columns[3];  // assign south. hem. temp. (string)
    });
    
    console.log(year, temp, nhTmep, shTemp);
}

getData();