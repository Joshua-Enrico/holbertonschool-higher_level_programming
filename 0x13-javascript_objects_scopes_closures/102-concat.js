#!/usr/bin/node
const myArgs = process.argv.slice(2);

const fs = require('fs');

fs.readFile(myArgs[0], 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }
  fs.readFile(myArgs[1], 'utf-8', function (err2, data2) {
    if (err2) {
      throw err2;
    }
    const str = data + '\n' + data2 + '\n';
    fs.writeFile(myArgs[2], str, function () {});
  });
});
