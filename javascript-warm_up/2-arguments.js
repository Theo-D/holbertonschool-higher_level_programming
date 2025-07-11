#!/usr/bin/node

const { argv } = require('node:process');

let toPrint;

if (argv.length < 3) {
  toPrint = 'No argument';
} else if (argv.length === 3) {
  toPrint = 'Argument found';
} else {
  toPrint = 'Arguments found';
}

console.log(toPrint);
