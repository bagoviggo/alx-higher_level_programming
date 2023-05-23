#!/usr/bin/node

// Script that prints the number of movies where the // character “Wedge Antilles” is present.
// Args: API url - https://swapi-api.alx-tools.com/api/films/
// Usage: 4-starwars_count.js <API url>

const request = require('request');
const url = process.argv[2];
const wedgeId = '18';

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let wedgeCount = 0;

    data.results.forEach(({ characters }) => {
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        wedgeCount++;
      }
    });

    console.log(wedgeCount);
  } else {
    console.log(error);
  }
});
