#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const apiUrl = 'https://swapi.dev/api';
  const filmUrl = `${apiUrl}/films/${movieId}/`;

  return new Promise((resolve, reject) => {
    request(filmUrl, (err, _, body) => {
      if (err) {
        reject(err);
        return;
      }

      const charactersURL = JSON.parse(body).characters;
      const charactersPromises = charactersURL.map(url => {
        return new Promise((resolve, reject) => {
          request(url, (promiseErr, __, charactersReqBody) => {
            if (promiseErr) {
              reject(promiseErr);
              return;
            }
            resolve(JSON.parse(charactersReqBody).name);
          });
        });
      });

      Promise.all(charactersPromises)
        .then(names => resolve(names))
        .catch(allErr => reject(allErr));
    });
  });
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  getMovieCharacters(movieId)
    .then(names => console.log(names.join('\n')))
    .catch(error => console.error(error));
} else {
  console.log('Usage: node script.js <Movie ID>');
}
