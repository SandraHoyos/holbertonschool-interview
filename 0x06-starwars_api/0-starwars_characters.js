#!/usr/bin/node
/* prints all characters of star wars movie passed as commandline argument */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/?format=json';
request.get(url, function (response, body) {
  const film = (JSON.parse(body.body));
  character(film.characters);
});
const character = (people, i = 0) => {
  if (i === people.length) return;
  request.get(people[i], function (response, body) {
    // console.log(people[i]);
    console.log(JSON.parse(body.body).name);
    character(people, i + 1);
  });
};
