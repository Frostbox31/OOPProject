/* globals Chart:false, feather:false */

(function () {
    'use strict'
  
    feather.replace()
  
       // Graphs
       var ctx = document.getElementById('myChart')
       // eslint-disable-next-line no-unused-vars
       var myChart = new Chart(ctx, {
         type: 'line',
         data: {
           labels: [
           'Sundayst',
           'Monday2',
           'Tuesdayst',
           'Wednesday3',
           'Thursda3y',
           'Frida3y',
           'Satur3day'
         ],
           datasets: [{
             data: [
               15339,
               21345,
               18483,
               24003,
               23489,
               24092,
               12034
             ],
             lineTension: 0,
             backgroundColor: 'transparent',
             borderColor: '#007bff',
             borderWidth: 4,
             pointBackgroundColor: '#007bff'
           }]
         },
         options: {
           scales: {
             yAxes: [{
               ticks: {
                 beginAtZero: false
               }
             }]
           },
           legend: {
             display: false
           }
         }
       })

  })()
  