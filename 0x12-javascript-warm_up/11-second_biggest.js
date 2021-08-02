#!/usr/bin/node
const myArgs = process.argv.slice(2);
function compare (a, b) {
  return a - b;
}

if (myArgs.length === 0 || myArgs.length < 2) {
  console.log(0);
} else {
  let list = [];

  for (const arg in myArgs) {
    if (!isNaN(myArgs[arg])) {
      list.push(parseInt(myArgs[arg]));
    }
  }
  list = list.sort(compare);
  console.log(list[list.slice(2).length]);
}
