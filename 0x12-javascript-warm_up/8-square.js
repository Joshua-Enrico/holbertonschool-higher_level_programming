#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs[0] === undefined || isNaN(myArgs[0])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs; i++) {
    console.log('X'.repeat(myArgs));
  }
}
