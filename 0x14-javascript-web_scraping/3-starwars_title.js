#!/usr/bin/node

const axios = require('axios');
const starWars = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

function movieTitle (response) {
  console.log(response.data.title);
}

axios.get(starWars).then(movieTitle);
