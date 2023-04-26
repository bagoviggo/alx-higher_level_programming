#!/usr/bin/node
// Script that gets the contents of a webpage // stores it in a file // Args: <URL> to request //       <path> file path to store body response // Usage: ./5-request_store.js <URL> <path>  const request = require('request');
 const fs = require('fs');
 const url = process.argv[2];
 const filePath = process.argv[3];
 
 if (!error && response.statusCode === 200) {
     fs.writeFile(filepath, body, 'utf-8', (error) => {
         if (error) {
             console.error(error.message);
             return;
 
         }
 
     });
 
     console.log(`Body response written to ${filePath}`);
};
 
 

                                                                         
           