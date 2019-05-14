#!/usr/bin/node
const request = require('request');
request('http://swapi.co/api/films', function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.includes('https://swapi.co/api/people/18/', 0)
        ? count + 1
        : count;
    }, 0));
  }
});
