/*
  JavaScript script that fetches and prints how to say "Hello" depending on the language

  API service: https://www.fourtonfish.com/hellosalut/hello/
*/
$(document).ready(function() {
    $('#btn_translate').click(function() {
      const langCode = $('#language_code').val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`;
  
      $.ajax({
        url: apiUrl,
        type: 'GET',
        dataType: 'json',
        success: function(response) {
          $('#hello').text(response.hello);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.log('Error occurred while fetching data: ' + textStatus + ' ' + errorThrown);
        }
      });
    });
  });
  