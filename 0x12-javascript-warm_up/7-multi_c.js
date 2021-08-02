#!/usr/bin/node
const myArgs = process.argv.slice(2);
const str = 'C is fun';
if (myArgs[0] === undefined || isNaN(myArgs[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myArgs; i++) {
    console.log(str);
  }
}
