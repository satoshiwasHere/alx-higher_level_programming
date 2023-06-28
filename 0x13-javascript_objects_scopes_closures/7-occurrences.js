#!/usr/bin/node

/*
 * A function that returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const element of list) {
    if (element === searchElement) {
      occurences++;
    }
  }
  return occurences;
};
