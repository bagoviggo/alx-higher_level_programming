/**
 * Script that fetches the translation of "hello" in French
 * from URL: https://fourtonfish.com/hellosalut/?lang=fr
 */
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .done(function (response) {
      $('#hello').text(response.hello);
    })
    .fail(function (xhr, status, error) {
      console.log('Error occurred while fetching data:', error);
      $('#hello').text('Error occurred while fetching data');
    });
});
