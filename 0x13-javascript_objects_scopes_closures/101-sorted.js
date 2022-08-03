#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
let valArray = [];

for (let i = 0; i < Object.keys(dict).length; i++) {
  const key = Object.values(dict)[i];
  for (let j = 0; j < Object.keys(dict).length; j++) {
    if (Object.values(dict)[j] === key) {
      valArray.push(Object.keys(dict)[j]);
    }
  }
  newDict[key] = valArray;
  valArray = [];
}
console.log(newDict);
