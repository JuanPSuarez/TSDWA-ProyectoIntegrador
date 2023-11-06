document.addEventListener("DOMContentLoaded", function () {
  function mostrarMensajeRegistroExitoso() {
    const mensajeRegistroExitoso = document.getElementById("registroExitoso");
    mensajeRegistroExitoso.style.display = "block";
  }

  setTimeout(mostrarMensajeRegistroExitoso, 3000);
});
