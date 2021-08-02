#!/usr/bin/node
const myArgs = process.argv.slice(2);
function factorial (myArgs) {
  if (isNaN(myArgs[0])) {
    console.log(1);
  } else {
    let factorial = 1;
    for (let i = 1; i <= myArgs; i++) {
      factorial *= i;
    }
    return (factorial);
  }
}
console.log(factorial(parseInt(myArgs)));
