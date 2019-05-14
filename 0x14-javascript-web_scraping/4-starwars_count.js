#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    results.forEach(function (movie) {
      if (movie.characters.includes('https://swapi.co/api/people/18/', 0)) count++;
    });
    console.log(count);
  }
});
