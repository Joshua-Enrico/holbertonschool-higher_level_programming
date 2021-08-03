#!/usr/bin/node
exports.converter = function (base) {
  function conversor (number) {
    return number.toString(base);
  }
  return conversor;
};
