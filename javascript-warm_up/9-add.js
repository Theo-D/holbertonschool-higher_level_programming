#!/usr/bin/node

const { argv } = require('node:process');

const x = parseInt(argv[2]);
const y = parseInt(argv[3]);

console.log(x + y);
