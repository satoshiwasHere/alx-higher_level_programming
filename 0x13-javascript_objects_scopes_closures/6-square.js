#!/usr/bin/node

/**
 * A class Square defining a square and inherits from Square of 5-square.js
 */

module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let xr = 0; xr < this.height; xr++) console.log(c.repeat(this.width));
    }
  }
};
