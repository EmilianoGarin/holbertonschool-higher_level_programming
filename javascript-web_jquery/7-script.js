const $ = window.$;

$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    const characterName = data.name;
    $('#character').text(characterName);
  });
});
