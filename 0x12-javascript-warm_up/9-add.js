#!/usr/bin/node
const myArgs = process.argv.slice(2);
const a = myArgs[0];
const b = myArgs[1];
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  }
  return (parseInt(a) + parseInt(b));
}
console.log(add(a, b));
