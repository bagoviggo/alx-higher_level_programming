/**
 * Script that fetches and lists the title for all movies by using this URL:
 *  https://swapi-api.alx-tools.com/api/films/?format=json
 */
$(document).ready(function () {
  // Fetch the movies data
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Extract the movie titles from the response
    const movies = data.results.map(function (movie) {
      return movie.title;
    });

    // Append the movie titles to the list
    const $list = $('#list_movies');
    $.each(movies, function (index, title) {
      $list.append('<li>' + title + '</li>');
    });
  });
});
