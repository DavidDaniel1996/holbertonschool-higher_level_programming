#!/usr/bin/node

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count += 1;
};
let count = 0;
