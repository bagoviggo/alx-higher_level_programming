#!/usr/bin/node

// Script that gets the contents of a webpage
// stores it in a file
// Args: <URL> to request
//       <path> file path to store body response
// Usage: ./5-request_store.js <URL> <path>

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8');
  }
});

