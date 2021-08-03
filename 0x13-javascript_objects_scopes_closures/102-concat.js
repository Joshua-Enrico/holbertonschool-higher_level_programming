#!/usr/bin/node
const myArgs = process.argv.slice(2);

const fs = require('fs');

fs.readFile(myArgs[0], 'utf-8', function (err, data) {
  if (err) {
    throw err;
  }
  fs.readFile(myArgs[1], 'utf-8', function (err2, data2) {
    if (err2) {
      throw err2;
    }
    const str = data + data2;
    fs.writeFile(myArgs[2], str, function () {});
  });
});
/* #!/usr/bin/node
const myArgs = process.argv.slice(2);
const filea = myArgs[0];
const fileb = myArgs[1];
const filec = myArgs[2];

const fs = require('fs');

const texta = fs.readFileSync(filea, 'utf-8');
const textb = fs.readFileSync(fileb, 'utf-8');
fs.writeFileSync(filec, texta + '\n' + textb + '\n');
*/
