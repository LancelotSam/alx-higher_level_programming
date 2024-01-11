#!/usr/bin/node
// executes x times a function

exports.CallMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
