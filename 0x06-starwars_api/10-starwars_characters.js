#!/usr/bin/node

const request = require('request');

const args = process.argv.slice(2);

const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
async function characters (url) {
  try {
    const response = await request.get(url);
    const chars = response.data.characters;

    let i = 0;
    while (i < chars.length) {
      const res = await request.get(chars[i]);
      console.log(res.data.name);
      i++;
    }
  } catch (error) {
    console.error(error);
  }
}

characters(url);
