#!/usr/bin/node

// script prints a message depending of the number of arguments passed

const argc = process.argv.length;
if (argc > 3)
{
  console.log('Arguments found');
} else if (argc === 3)
{
  console.log('Argument found');
} else
{
  console.log('No argument');
}
