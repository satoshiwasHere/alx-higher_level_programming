#!/usr/bin/node

/*
 * A class Square that defines a square and inherits from Square of 5-square.js
 */ 

const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    this.print(c);
  }
}

module.exports = Square;
