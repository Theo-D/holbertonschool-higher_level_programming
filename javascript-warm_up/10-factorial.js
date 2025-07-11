#!/usr/bin/node

const { argv } = require('node:process');

const num = argv[2];

function fact (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

console.log(fact(num));
