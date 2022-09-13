#!/usr/bin/node

const fs = require('fs');

function readData (data) {
  console.log(data);
}

fs.readFile(process.argv[2], 'utf-8', readData);
