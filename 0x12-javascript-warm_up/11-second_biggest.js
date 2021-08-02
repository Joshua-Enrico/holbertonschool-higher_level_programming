#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs.length > 1) {
  let list = [];

  for (const arg in myArgs) {
    if (!isNaN(myArgs[arg])) {
      list.push(parseInt(myArgs[arg]));
    }
  }
  list = list.sort();
  console.log(list[list.slice(2).length]);
} else {
  console.log(0);
}
