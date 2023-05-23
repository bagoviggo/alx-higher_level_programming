#!/usr/bin/node

// Script to display status code of a GET request
// Usage: ./2-statuscode.js <url>

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
