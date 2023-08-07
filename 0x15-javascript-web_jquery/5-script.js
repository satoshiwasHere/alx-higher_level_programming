$(document).ready(function () {
  $('#add_item').click(function () {
    const newEl = $('<li></li>').text('Item');
    $('ul.my_list').append(newEl);
  });
});
