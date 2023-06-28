#!/usr/bin/node

/**
 * Writes a class Rectangle that defines a rectangle:
 */

module.exports = class Rectangle {

  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let vr = 0; vr < this.height; vr++) console.log('X'.repeat(this.width));
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
