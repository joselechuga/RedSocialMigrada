$("#chatuno_1").hide();
$("#chatdos_2").hide();
$("#persona1").hide();
$("#persona2").hide();


$("#boton1").click(function(){
    $("#chatuno_1").fadeIn();
    $("#fotosinchat").fadeOut();
    $("#chatdos_2").fadeOut();
    $("#persona").fadeOut();
    $("#persona1").fadeIn();
    $("#persona2").fadeOut();
});

$("#boton2").click(function(){
    $("#chatuno_1").fadeOut();
    $("#chatdos_2").fadeIn();
    $("#fotosinchat").fadeOut();
    $("#persona").fadeOut();
    $("#persona1").fadeOut();
    $("#persona2").fadeIn();

});