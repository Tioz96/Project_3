$(document).ready(function() {
    // Obtener los campos disponibles desde la API Flask
    $.getJSON('/api/campos', function(data) {
      var campoDropdown = $('#campo-dropdown');
  
      // Generar las opciones del dropdown list
      $.each(data.campos, function(index, campo) {
        campoDropdown.append($('<option>', {
          value: campo,
          text: campo
        }));
      });
    });
  
    // Capturar la selección del usuario y generar la gráfica correspondiente
    $('#generar-grafica').click(function(event) {
      event.preventDefault();
  
      var campoSeleccionado = $('#campo-dropdown').val();
  
      if (campoSeleccionado) {
        // Realizar una solicitud a la API Flask para obtener los datos de la gráfica
        $.getJSON('/api/datos?campo=' + campoSeleccionado, function(data) {
          // Procesar los datos y crear la gráfica utilizando Chart.js
          // ... Código para crear la gráfica ...
        });
      }
    });
  });