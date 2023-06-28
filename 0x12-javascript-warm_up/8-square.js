#!/usr/bin/node

// script that prints a square

const x = process.argv[2];
if (!parseInt(x)) {
  console.log('Missing size');
} else {
  for (let sz = 0; sz < x; sz++) {
    let vr = 0;
    let myVar = '';

    while (vr < x) {
      myVar = myVar + 'X';
      vr++;
    }
    console.log(myVar);
  }
}
