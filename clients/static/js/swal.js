  // Obtener todos los botones de eliminar
  const eliminarBtns = document.querySelectorAll("#eliminar-elemento");
/*   const sendMailBtn = document.querySelector("#send_mail");

  sendMailBtn.addEventListener("click", function (event) {
      
  
      Swal.fire({
          title: "Correo enviado",
          text: "Los correos electrónicos se enviaron correctamente",
          icon: "success",
          confirmButtonText: "Ok"
      });
  }); */
  // Agregar un evento click a cada botón de eliminar
  eliminarBtns.forEach(function(el) {
    el.addEventListener("click", function (event) {
      // Prevenir la acción predeterminada del botón
      event.preventDefault();

      // Obtener la URL de eliminación del atributo data-url
      const url = el.getAttribute("data-url");

      // Mostrar un mensaje de confirmación utilizando Sweet Alert
      Swal.fire({
        title: "¿Estás seguro que deseas eliminar este elemento?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
      }).then((result) => {
        // Si el usuario confirma la eliminación
        if (result.isConfirmed) {
          // Crear un formulario para enviar la solicitud de eliminación
          const form = document.createElement("form");
          form.method = "POST";
          form.action = url;

          // Agregar el token CSRF al formulario
          const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0];
          const csrfInput = document.createElement("input");
          csrfInput.type = "hidden";
          csrfInput.name = "csrfmiddlewaretoken";
          csrfInput.value = csrfToken.value;
          form.appendChild(csrfInput);

          // Agregar un campo oculto para indicar que la solicitud es para eliminar
          const deleteInput = document.createElement("input");
          deleteInput.type = "hidden";
          deleteInput.name = "delete";
          deleteInput.value = "true";
          form.appendChild(deleteInput);

          // Enviar la solicitud de eliminación
          document.body.appendChild(form);
          form.submit();
        }
      });
    });
  });