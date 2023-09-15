document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      const translation = data.hello;
      helloElement.textContent = translation;
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
});
