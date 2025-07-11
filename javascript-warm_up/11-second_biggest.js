#!/usr/bin/node

const { argv } = require('node:process');
const size = argv.length;
let num = 0;

function toInt (currVal, index, arr) {
  arr[index] = parseInt(arr[index]);
}

function findSecond (arr) {
  let max = 0;
  let second = 0;
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] >= max) {
      second = max;
      max = arr[i];
    } else if (arr[i] > second) {
      second = arr[i];
    }
  }
  return second;
}

if (size > 3) {
  argv.forEach(toInt);
  num = findSecond(argv);
}

console.log(num);
