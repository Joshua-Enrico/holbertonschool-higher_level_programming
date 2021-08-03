const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (C) {
    if (C === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};
