#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (myArgs.length === 0 || myArgs.length < 2) {
  console.log(0);
} else {
  let list = [];

  for (const arg in myArgs) {
    list.push(parseInt(myArgs[arg]));
  }
  list = list.sort();
  console.log(list);
  console.log(list[list.slice(2).length]);
}
