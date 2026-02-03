/* JSON Demonstration Using COVID-19 Data
   Populate HTML by dynamically adding rows
 */

async function getData() {
  // Define variables to store the data
  const state = [];
  const positive = [];
  const currentlyHospitalized = [];

  const tbodyEl = document.querySelector("tbody"); // Select the <tbody> element
  // querySelector retrieves an element using any valid CSS selector (class, id, or tag)
    // Return a static node list which supports array methods (ex: forEach)
    // Newer method compared to getElementById()
    // Grabs the first element that meets the criteria

  // getElementById() only selects elements by id.
  // getElementById() returns an HTML collection that changes as the DOM (Document Object Model) changes.

  const data = await fetch("covid19.json")
    .then(data => data.json())
    .then(data => {
      // console.log(data);

      // Push JSON data to JS arrays & display in a table
      for (let i = 0; i < data.length; i++) {
        state.push(data[i].state);
        positive.push(data[i].positive);
        currentlyHospitalized.push(data[i].hospitalizedCurrently);
        console.log(state[i], positive[i]);

        // Dynamically generate HTML table (add rows via string interpolation)
        tbodyEl.innerHTML += `
          <tr>
            <td class="state">${state[i]}</td>
            <td class="positive">${positive[i]}</td>
          </tr>
        `
      }
    });
  
  return { state, positive, currentlyHospitalized };
}

async function createChart() {
    const data = await getData();   // createChart will wait for getData() to process CSV info
    const chart = document.getElementById('covidChart');
    const myChart = new Chart(chart, {  // Construct the chart    
        type: 'line',
        data: {                         // Define data
            labels: data.state,        // x-axis labels
            datasets: [                 // Each object describes one dataset of y-values
                                        //  including display properties.  To add more datasets, 
                                        //  place a comma after the closing curly brace of the last
                                        //  data set object and add another dataset object. 
                {
                    label:    `Positive Cases (6/13/20)`,     // Dataset label for legend
                    data:     data.positive,
                    fill:     false,           // Fill area under the linechart (true = yes, false = no)
                    backgroundColor:  'rgba(0, 200, 0, 0.2)',    // Color for data marker
                    borderColor:      'rgba(0, 200, 0, 1)',      // Color for data marker border
                    borderWidth:      1,   // Data marker border width
                }
        ]
        },
        options: {                        // Define display chart display options 
            responsive: true,             // Re-size based on screen size
            maintainAspectRatio: false,
            scales: {                     // Display options for x & y axes
                x: {                      // x-axis properties
                    title: {
                        display: true,
                        text: 'State',     // x-axis title
                        font: {                   // font properties
                            size: 16
                        },
                        color: 'black'
                    },
                    ticks: {                      // x-axis tick mark properties
                        min: 0,
                        font: {
                            size: 12
                        },
                        color: 'black'
                    },
                    grid: {                       // x-axis grid properties
                        display: false
                    }
                },
                y: {                              // y-axis properties
                    title: {
                        display: true,                          
                        text: `COVID-19 Positive Cases`,     // y-axis title
                        font: {
                            size: 16
                        },
                        color: 'black'
                    },
                    ticks: {
                        min: 0,                   
                        maxTicksLimit: data.positive.length / 5,        // Actual value can be set dynamically
                        font: {
                            size: 12
                        },
                        color: 'black'
                    },
                    grid: {                       // y-axis gridlines
                        color: '#6c767e'
                    }
                }
            },
            plugins: {                  // Display options for title and legend
                title: {
                    display: true,
                    text: 'COVID-19 Positive Cases by State',
                    font: {
                        size: 24
                    },
                    color: '#black',
                    padding: {
                        top: 10,
                        bottom: 30
                    }
                },
                legend: {
                    align: 'middle',
                    position: 'top',
                    labels: {
                        color: 'black'
                    }
                }
            }
        }       
    });
  
  const sumCases = data.positive.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  const avgCases = sumCases / data.positive.length;

  const sumCurrHospitalized = data.currentlyHospitalized.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
  const avgCurrHospitalized = sumCurrHospitalized / data.currentlyHospitalized.length;
  
  document.getElementById('averageCases').innerHTML = `Average of Positive Cases: <strong>${avgCases.toFixed(0)}</strong>`;
  document.getElementById('averageHospitalized').innerHTML = `Average of Currently Hospitalized: <strong>${avgCurrHospitalized.toFixed(0)}</strong>`;
}

createChart();