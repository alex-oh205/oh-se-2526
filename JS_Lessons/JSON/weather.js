/* JSON Demonstration Using Lincroft Weather Data
    1.  Temperatures in Kelvin
    2.  Humidity in %
    3.  Atmospheric Pressue:  hPa = Pa x 100
    4.  Wind Speed: m/s
    5.  Cloudiness: %
    6.  Rain:  mm       Had to convert key "1h" to "h1" (Can't follow # with letter in JS)
 */

async function getData() {

    // Define arrays to store data
    const temperature = [];
    const humidity = [];
    const pressure = [];
    const windSpeed = [];
    const rain = [];
    const weather = [];
    const icon = [];

    const data = await fetch('weather.json')
        .then(data => data.json())
        .then(data => {
            console.log(data);

            // Push JSON data to JS arrays
            temperature.push(data.main.temp);
            humidity.push(data.main.humidity);
            pressure.push(data.main.pressure);
            windSpeed.push(data.wind.speed);
            rain.push(data.rain.h1);
            weather.push(data.weather[0].description);
            icon.push(data.weather[0].icon);
            console.log(weather);
            
            // Display JSON data in HTML table
            document.getElementById("temperature").innerHTML = `Temperature: ${temperature[0]} K`;
            document.getElementById("humidity").innerHTML = `Humidity: ${humidity[0]} %`;
            document.getElementById("pressure").innerHTML = `Pressure: ${pressure[0]} hPa`;
            document.getElementById("windSpeed").innerHTML = `Wind Speed: ${windSpeed[0]} m/s`;
            document.getElementById("rain").innerHTML = `Rain (last 1 hr): ${rain[0]} mm`;

            // Set weather icon
            document.getElementById("weather").innerHTML = `<img src="img/${icon[0]}.png" alt="rain", width="75">`;

            console.log(temperature, humidity, pressure, windSpeed, rain, icon);
        });
}

getData();