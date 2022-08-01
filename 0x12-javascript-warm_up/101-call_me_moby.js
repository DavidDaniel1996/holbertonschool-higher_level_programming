#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let idx = 0;
  while (idx < x) {
    theFunction();
    idx += 1;
  }
};
