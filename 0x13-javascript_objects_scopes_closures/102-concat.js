#!/usr/bin/node

const fs = require('fs');

let dataA;
let dataB;

try {
  dataA = fs.readFileSync(process.argv[2], 'utf8');
} catch (err) {
  console.error(err);
}

try {
  dataB = fs.readFileSync(process.argv[3], 'utf8');
} catch (err) {
  console.error(err);
}

const content = dataA + dataB;

try {
  fs.writeFileSync(process.argv[4], content);
} catch (err) {
  console.error(err);
}
