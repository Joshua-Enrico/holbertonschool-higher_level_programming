#!/usr/bin/node
const myArgs = process.argv.slice(2);
let Sbiggest = 0;
if (myArgs.length > 1) {
  myArgs.sort();
  Sbiggest = (myArgs[myArgs.slice(2).length]);
}
console.log(Sbiggest);
