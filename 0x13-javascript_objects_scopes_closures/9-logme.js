#!/usr/bin/node
let StaticVar = 0;
exports.logMe = function (item) {
  console.log(StaticVar + ': ' + item);
  StaticVar++;
};
