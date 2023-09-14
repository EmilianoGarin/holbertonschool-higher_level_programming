document.addEventListener("DOMContentLoaded", function () {
    // Obtén el elemento con el id "red_header"
    const redHeader = document.getElementById("red_header");
  
    // Agrega un evento de clic al elemento
    redHeader.addEventListener("click", function () {
      // Obtén el elemento del encabezado
      const header = document.querySelector("header");
  
      // Agrega la clase "red" al elemento del encabezado
      header.classList.add("red");
    });
});