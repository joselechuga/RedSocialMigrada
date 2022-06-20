        
$(document).ready(function() {
    /**OCULTAR SPAN DE ERROR NOMBRE */
    $(".error_nombre").hide();/**Debe ingresar nombre y apellido */

    /**OCULTAR SPAN DE NOMBRE OBLIGATORIO */
    $(".sn_nomap").hide(); /**Este campo es obligatorio */

    /**OCULTAR CHEC CORRECTO NOMBRE ✔ */
    $(".nom_correcto").hide();

    /**OCULTAR SPAN DE ERROR CORREO */
    $(".sn_correo").hide();/**Debe introducir su correo electrónico. */


    $("#errorcomentario").hide()




    /**EVITA  QUE LA TECLA ENTER MANDE EL FORMULARIO AUTOMATICAMENTE */
    window.addEventListener("keypress", function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
        }
    }, false);


    
/**COLORES AL INTERACTUAR CON EL FORMULARIO */

    $(".input").click(function () {
        /**AL MOMENTO DE DAR CLICK EN INPUT NOMBRE PASA A ROJO EXIGIENDO EL CAMPO*/
        /**SI EL TEXTO ES IGUAL A 0 O NO TIENE TEXTO */
        if ($("#nombre").val().length == 0) {
            $("#nombre").css({ background: "#fe8c8c" });
            $(".sn_nomap").show().css({ color: "red" });
            $(".error_nombre").hide();
            $(".nom_correcto").hide();
            return false;
        }
    
    
    
        /**CONDICION DE NOMBRE INCOMPLETO */
        if ($("#nombre").val().length <= 7) {
            $(".sn_nomap").hide();
            $(".nom_correcto").hide();
            $(".error_nombre").show().css({ color: "red" });
    
        }
    
        /**CONDICION DE NOMBRE CORRECTO */
    
        if ($("#nombre").val().length > 10) {
            $(".nom_correcto").show().css({ color: "green" });
            $(".sn_nomap").hide();
            $(".error_nombre").hide();
            $("#nombre").css({ background: "white" });
        }

        
          //Correo

          if ($("#email").val().length == 0) {
            $("#email").css({ background: "#fe8c8c" });
            $(".sn_correo").show();
            $("#error").hide();
            $("#success").hide();
        }
        

        $('#email').on('keyup', function() {
            var re = /([A-Z0-9a-z_-][^@])+?@[^$#<>?]+?\.[\w]{2,4}/.test(this.value);
            if(!re) {
                $('#error').show();
                $('#success').hide();
                $(".sn_correo").hide();
                $("#email").css({ background: "white" });
            } else {
                $('#error').hide();
                $('#success').show();
                $(".sn_correo").hide();
                $("#email").css({ background: "white" });
            }
        });

       

        
    });
    




    $('#enviar').click(function(){
        //Nombre

        
        if ($("#nombre").val().length < 10) {
            alert("Debe indicar su nombre y apellido.");
            $("#nombre").css({ background: "#fe8c8c" });
            $(".sn_nomap").show().css({ color: "red" });
            $(".error_nombre").hide();
            return false;
        }


        // El input que queremos validar
        const input = document.forms['validationForm']['nombre'];
    
        // El pattern que vamos a comprobar
        const pattern = new RegExp('^[A-Z]+$', 'i');
    
      // Por último, nuestra función que verifica si el campo es válido antes de realizar cualquier otra acción.
        if (input != pattern ) {
          alert('SOLO LETRAS EN EL CAMPO "NOMBRE"');
          return false;
        } 

        //Correo

        if ($("#email").val().length < 1) {
            alert("Debe introducir su correo electrónico.");
            $("#email").css({ background: "#fe8c8c" });
            $(".sn_correo").show();
            $("#error").hide();
            $("#success").hide();
            return false
        }

        if($("#comentario").val().length < 30){
            alert("minimo 30 caracteres");
            $("#comentario").css({ background: "#fe8c8c" });
            $("#errorcomentario").show().css({color:"red"});
            return false
        }


    });
    });

    $("#contenedor2").hide();
    $("#mostrar").click(function(){

    });