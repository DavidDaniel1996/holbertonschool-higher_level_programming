#!/usr/bin/node

let idx = 0;
const num = Number(Math.floor(process.argv[2]));

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (idx < num) {
    console.log('C is fun');
    idx += 1;
  }
}
