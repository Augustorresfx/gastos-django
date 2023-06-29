/* globals Chart:false, feather:false */

(function () {

    //data
    let enero = document.getElementById('enero')
    let febrero = document.getElementById('febrero')
    let marzo = document.getElementById('marzo')
    let abril = document.getElementById('abril')
    let mayo = document.getElementById('mayo')
    let junio = document.getElementById('junio')
    let julio = document.getElementById('julio')
    let agosto = document.getElementById('agosto')
    let septiembre = document.getElementById('septiembre')
    let octubre = document.getElementById('octubre')
    let noviembre = document.getElementById('noviembre')
    let diciembre = document.getElementById('diciembre')
  // Graphs
    let ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        legend: "Estadísticas",
        labels: [
          'Enero',
          'Febrero',
          'Marzo',
          'Abril',
          'Mayo',
          'Junio',
          'Julio',
          'Agosto',
          'Septiembre',
          'Octubre',
          'Noviembre',
          'Diciembre'
        ],
        datasets: [{
          data: [
            enero.value,
            febrero.value,
            marzo.value,
            abril.value,
            mayo.value,
            junio.value,
            julio.value,
            agosto.value,
            septiembre.value,
            octubre.value,
            noviembre.value,
            diciembre.value
          ],
          lineTension: 2000,
          backgroundColor: '#96B2CE',
          borderColor: '#007bff',
          borderWidth: 1,
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
  