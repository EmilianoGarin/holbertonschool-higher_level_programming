const $ = window.$;

$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    $.each(movies, function (index, movie) {
      $('#list_movies').append($('<li>').text(movie.title));
    });
  });
});
