#!/usr/bin/node
exports.addMeMaybe = function (times, func) {
  func(times += 1);
};
