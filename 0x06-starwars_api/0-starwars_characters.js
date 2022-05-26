#!/usr/bin/node
/* prints all characters of star wars */

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const arrayPersonajes = (JSON.parse(res.body).characters);

  for (const personaje of arrayPersonajes) {
    await new Promise((resolve, reject) => {
      request(personaje, (err, res, body) => {
        err && console.log(err);
        console.log(JSON.parse(body).name);
        resolve();
      }
      );
    });
  }
});
