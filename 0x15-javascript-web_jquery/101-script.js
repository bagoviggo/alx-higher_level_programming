$(document).ready(function() {
    // Add item to the list
    $('#add_item').on('click', function() {
      $('.my_list').append('<li>Item</li>');
    });
  
    // Remove last item from the list
    $('#remove_item').on('click', function() {
      $('.my_list li:last-child').remove();
    });
  
    // Clear the entire list
    $('#clear_list').on('click', function() {
      $('.my_list').empty();
    });
  });
  