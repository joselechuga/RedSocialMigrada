$(document).ready(function(){
    $("#enviar").click(function(){
      /**llamar link de datos*/
        $.getJSON('https://mindicador.cl/api', function(data) {
    var dailyIndicators = data;
    $("<p/>", {
        html: 'El valor actual del RP es $' + dailyIndicators.uf.valor
    }).appendTo("#precio");
}).fail(function() {
    console.log('Error al consumir la API!');
});
    });
});

