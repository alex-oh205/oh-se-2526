// This program will simulate a network request
// and will show why async functions are needed

// Output: Program will return "Processing Picture"
// before it's downloaded

function download(url, callback) {
    setTimeout(() => {

        // script to download picture
        console.log(`Downloading ${url}`);

        // Process the picture after downloading
        callback(url);
    }, 2000); // 2000 = wait time in milliseconds
}

// function to process the picture
function process(picture) {
    console.log(`Processing ${picture}`);
}

let url = 'https://www.hths.mcvsd.org/o/hths/article/2253921';

download(url, process);