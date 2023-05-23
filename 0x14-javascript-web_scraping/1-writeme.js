#!/usr/bin/node

// Script that writes to a file
// Usage: ./1-writeme.js <path> <file>

const fs = require('fs');
const path = process.argv[2];
const string = process.argv[3];

fs.writeFile(path, string, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
