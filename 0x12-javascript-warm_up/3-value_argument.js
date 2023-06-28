#!/usr/bin/node

// script prints the first argument passed to it

console.log(process.argv[2] ? process.argv[2] : 'No argument');
