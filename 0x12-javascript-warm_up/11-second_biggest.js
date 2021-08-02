#!/usr/bin/node
const myArgs = process.argv.slice(2);
let Sbiggest = 0;
if (myArgs.length > 1) {
  let list = [];

  for (const arg in myArgs) {
    if (!isNaN(myArgs[arg])) {
      list.push(parseInt(myArgs[arg]));
    }
  }
  list = list.sort();
  Sbiggest = (list[list.slice(2).length]);
}
console.log(Sbiggest);
