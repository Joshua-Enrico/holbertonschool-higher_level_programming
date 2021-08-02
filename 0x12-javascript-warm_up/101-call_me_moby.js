#!/usr/bin/node
exports.callMeMoby = function (times, func) {
  for (let i = 0; i < times; i++) {
    func();
  }
};
