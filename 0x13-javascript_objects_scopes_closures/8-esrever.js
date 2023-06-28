#!/usr/bin/node

/**
 * A function that returns the reversed version of a list
 */

exports.esrever = function (list) {
  const reversedList = [];
  for (let xr = list.length - 1; xr >= 0; xr--) {
    reversedList.push(list[xr]);
  }

  return (reversedList);
};
