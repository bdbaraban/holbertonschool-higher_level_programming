#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map(item => item * list.indexOf(item));
console.log(list);
console.log(newList);
