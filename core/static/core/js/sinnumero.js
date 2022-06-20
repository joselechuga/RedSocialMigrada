 // La siguiente funcion valida el elemento input

    // Variable que usaremos para determinar si el input es valido
    let isValid = false;

    // El input que queremos validar
    const input = document.forms['validationForm']['nombre'];

    input.willValidate = false;

    // El pattern que vamos a comprobar
    const pattern = new RegExp('^[A-Z]+$', 'i');

  // Por último, nuestra función que verifica si el campo es válido antes de realizar cualquier otra acción.
    if (!input ) {
      alert('El campo no es válido.');
    } else {
      alert('El campo es válido');
    }
  