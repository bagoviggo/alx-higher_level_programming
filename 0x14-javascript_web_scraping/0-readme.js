#!/usr/bin/node

// A Script that reads and prints content of a file.
// Usage: ./0-reame.js <file>

let fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf-8', (error, data) => {
    if (error) throw error;
    console.log(data);
});

