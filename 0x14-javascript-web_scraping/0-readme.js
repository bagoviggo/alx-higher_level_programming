#!/usr/bin/node

// A Script that reads and prints content of a file.
// Usage: ./0-reame.js <file>

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});

