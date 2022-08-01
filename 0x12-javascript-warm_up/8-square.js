#!/usr/bin/node

let idx = 0;
const num = Number(Math.floor(process.argv[2]));

if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (idx < num) {
    console.log('X'.repeat(num));
    idx += 1;
  }
}
