#!/usr/bin/node

function factorial (number) {
  if (number === 1) {
    return (1);
  }
  return (number * factorial(number - 1));
}

const num = Number(Math.floor(process.argv[2]));

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
