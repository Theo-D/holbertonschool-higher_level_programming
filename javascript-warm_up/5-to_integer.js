#!/usr/bin/node

const { argv } = require('node:process');
const num = parseInt(argv[2]);

if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
