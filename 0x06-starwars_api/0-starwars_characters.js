#!/usr/bin/node

const request = require('request');

const args = process.argv.slice(2);

const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
async function characters (url) {
  try {
    request.get(url, (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        const chars = JSON.parse(body).characters;

        const i = 0;
        const fetchCharacter = (index) => {
          if (index >= chars.length) return;
          request.get(chars[index], (err, res, character) => {
            if (err) {
              console.error(err);
            } else {
              console.log(JSON.parse(character).name);
              fetchCharacter(index + 1);
            }
          });
        };

        fetchCharacter(i);
      }
    });
  } catch (error) {
    console.error(error);
  }
}

characters(url);
