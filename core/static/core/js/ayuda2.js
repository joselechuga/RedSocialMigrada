$(function(){

$("#contenedor2").hide();
    
$("#mostrar").click(function(){
    $("#contenedor2").fadeIn();
        });

        $("#ocultar").click(function(){
            $("#contenedor2").fadeOut();
                });
});



$("#d2").hide();


$('#bt1').click(function(){
    $("#d1").hide();
    $("#d2").show();
});