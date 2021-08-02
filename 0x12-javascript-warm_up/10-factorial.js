#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (isNaN(myArgs[0])) {
  console.log(1);
} else {
  let factorial = 1;
  for (let i = 1; i <= myArgs; i++) {
    factorial *= i;
  }
  console.log(factorial);
}
