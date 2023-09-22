const $ = window.$;

$('#add_item').click(function () {
  const newItem = $('<li>').text('Item');
  $('ul.my_list').append(newItem);
});
