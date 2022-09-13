#!/usr/bin/node

const fs = require('fs');

function printError (err) {
  if (err) {
    console.log(err);
  }
}

fs.writeFile(process.argv[2], process.argv[3], printError);
