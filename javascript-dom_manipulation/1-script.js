document.addEventListener("DOMContentLoaded", function () {
    // Obtén el elemento con el id "red_header"
    const redHeader = document.getElementById("red_header");
  
    // Agrega un evento de clic al elemento
    redHeader.addEventListener("click", function () {
        // Cambia el color del texto del encabezado a rojo (#FF0000)
        document.querySelector("header").style.color = "#FF0000";
        });
    });
