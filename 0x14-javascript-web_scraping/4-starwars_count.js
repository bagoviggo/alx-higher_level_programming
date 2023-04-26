#!/usr/bin/node

// Script that prints the number of movies where the // character “Wedge Antilles” is present.
// Args: API url - https://swapi-api.alx-tools.com/api/films/
// Usage: 4-starwars_count.js <API url>

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body);
    let count = 0;
    for (const filmIndex in films) {
      const filmChars = films[filmIndex].characters;

      for (const characterIndex in filmChars) {
        if (filmChars[characterIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error: Status code ' + response.status);
  }
});
