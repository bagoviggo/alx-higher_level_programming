#!/usr/bin/node

// A script that prints title of Star wars movie where episode coincides
// with the given integer(id)
// Args: id - int that will represent the episode number
// Usage: ./3-starwars_title.js <id>

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/${id}';

request (url, (error, response, body) => {
    if (!error && response.response.statusCode === 200) {
        const info = JSON.parse(body);
        console.log(info.title)
    } 
});

