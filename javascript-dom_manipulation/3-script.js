document.addEventListener('DOMContentLoaded', function () {
  const toggleHeader = document.getElementById('toggle_header');
  const header = document.querySelector('header');

  toggleHeader.addEventListener('click', function () {
    header.classList.toggle('red');
    header.classList.toggle('green');
  });
});
