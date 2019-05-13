#!/usr/bin/node
const nbOccurences = require('../7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(['H', 12, 'c', 'H', 'Holberton', 8], 'H'));
