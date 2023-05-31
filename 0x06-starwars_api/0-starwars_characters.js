#!/usr/bin/node

import axios from 'axios';

const args = process.argv.slice(2);

const url = `https://swapi-api.alx-tools.com/api/films/${args[0]}`;
async function characters (url) {
  try {
    const response = await axios.get(url);
    const chars = response.data.characters;

    let i = 0;
    while (i < chars.length) {
      const res = await axios.get(chars[i]);
      console.log(res.data.name);
      i++;
    }
  } catch (error) {
    console.error(error);
  }
}

characters(url);
