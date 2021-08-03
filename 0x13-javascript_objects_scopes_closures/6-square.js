#!/usr/bin/node
const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  charPrint (C) {
    if (C === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(C.repeat(this.height));
      }
    }
  }
};
