#!/usr/bin/node
const initialList = require('./100-data.js').list;
const newList = initialList.map(item => item * initialList.indexOf(item));
console.log(initialList);
console.log(newList);
