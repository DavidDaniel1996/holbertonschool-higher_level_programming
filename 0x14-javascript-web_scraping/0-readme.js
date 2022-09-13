#!/usr/bin/node

const fs = require('fs');

function readData (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
}

fs.readFile(process.argv[2], 'utf-8', readData);
