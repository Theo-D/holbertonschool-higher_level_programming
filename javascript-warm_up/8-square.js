#!/usr/bin/node

const { argv } = require('node:process');
const times = parseInt(argv[2]);

if (isNaN(times)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < times; i++) {
    console.log('X'.repeat(times));
  }
}
