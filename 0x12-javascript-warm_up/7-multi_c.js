#!/usr/bin/node

// script that prints x times “C is fun

const x = Math.floor(Number(process.argv[2]));

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let rs = 0; rs < x; rs++) {
    console.log('C is fun');
  }
}
