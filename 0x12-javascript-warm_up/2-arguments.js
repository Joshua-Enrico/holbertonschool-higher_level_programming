#!/usr/bin/node
const myArgs = process.argv.slice(2);
const length = myArgs.length;

if (length <= 0) {
  console.log('No argument');
}
if (length === 1) {
  console.log('Argument found');
}
if (length > 1) {
  console.log('Arguments found');
}
