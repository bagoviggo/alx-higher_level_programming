/**
 * Script to fetch the character name from the provided URL and
 * display it in the HTML tag <div id="character">,
*/
$(document).ready(function () {
  // AJAX request to the URL
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Extract the character name from the response JSON
      const characterName = data.name;

      // Update the text of the <div id="character"> element with the character name
      $('#character').text(characterName);
    },
    error: function () {
      // Handle any errors that occur during the AJAX request
      console.log('Error: Unable to fetch character data.');
    }
  });
});
