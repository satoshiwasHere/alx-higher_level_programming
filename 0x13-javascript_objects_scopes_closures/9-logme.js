#!/usr/bin/node

/**
 * function printing the no of arguments already printed plus new argument value
 */

let count = 0;

exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
