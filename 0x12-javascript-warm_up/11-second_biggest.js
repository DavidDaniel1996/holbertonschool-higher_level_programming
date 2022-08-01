#!/usr/bin/node

const array = process.argv.sort((a, b) => b - a);

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(array[3]);
}
