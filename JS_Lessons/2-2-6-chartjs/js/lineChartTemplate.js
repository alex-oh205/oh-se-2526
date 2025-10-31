/* 
   Line Chart Template
*/
      
const lineChart = document.getElementById('lineChart');     // Get the html element that will hold the chart
    
const myChart = new Chart(lineChart, {  // Construct the chart    
    type: 'line',
    data: {                         // Define data
        labels: data.xYears,        // x-axis labels
        datasets: [                 // Each object describes one dataset of y-values
                                    //  including display properties.  To add more datasets, 
                                    //  place a comma after the closing curly brace of the last
                                    //  data set object and add another dataset object. 
            {
                label:    'Dataset 1',     // Dataset label for legend
                data:     data.yValues,    // Reference to array of y-values
                fill:     false,           // Fill area under the linechart (true = yes, false = no)
                backgroundColor:  'rgba(255, 0, 132, 0.2)',    // Color for data marker
                borderColor:      'rgba(255, 0, 132, 1)',      // Color for data marker border
                borderWidth:      1   // Data marker border width
            },
    ]
    },
    options: {                        // Define display chart display options 
        responsive: true,             // Re-size based on screen size
        maintainAspectRatio: false,
        scales: {                     // Display options for x & y axes
            x: {                      // x-axis properties
                title: {
                    display: true,
                    text: 'x-axis title',     // x-axis title
                    font: {                   // font properties
                        size: 14
                    },
                },
                ticks: {                      // x-axis tick mark properties
                min: 0,                     // starting value      
                font: {
                    size: 14  
                },
                },
                grid: {                       // x-axis grid properties
                    color: '#6c767e'
                }
            },
            y: {                              // y-axis properties
                title: {
                    display: true,                          
                    text: 'y-axis title',     // y-axis title
                    font: {
                        size: 14
                    },
                },
                ticks: {
                    min: 0,                   
                    maxTicksLimit: 20,        // Actual value can be set dynamically
                    font: {
                        size: 12
                    }
                },
                grid: {                       // y-axis gridlines
                    color: '#6c767e'
                }
            }
        },
        plugins: {                  // Display options for title and legend
            title: {
                display: true,
                text: 'Global Mean Temperature vs. Year (since 1880)',
                font: {
                    size: 24,
                },
                color: '#black',
                padding: {
                    top: 10,
                    bottom: 30
                }
            },
            legend: {
                align: 'start',
                position: 'bottom',
            }
        }
    }       
});
  
