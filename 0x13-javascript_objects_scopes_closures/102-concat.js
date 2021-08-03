#!/usr/bin/node
const myArgs = process.argv.slice(2);
const filea = myArgs[0];
const fileb = myArgs[1];
const filec = myArgs[2];

const fs = require('fs');

const texta = fs.readFileSync(filea, 'utf-8');
const textb = fs.readFileSync(fileb, 'utf-8');
fs.writeFileSync(filec, texta + '\n' + textb + '\n');
