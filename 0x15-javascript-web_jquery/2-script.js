/* Script updates <header> when user clicks on <div #red_header>
 (document).ready ensures script runs DOM fully loaded */
$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
