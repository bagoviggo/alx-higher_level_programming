/* Script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:
 */
$(document).ready(function () {
  $('#add_item').click(function () {
    // Create a new <li> element with the text content "Item"
    const newItem = $('<li>').text('Item');

    // Append the new <li> element to UL.my_list
    $('ul.my_list').append(newItem);
  });
});
