#!/usr/bin/node

const axios = require('axios');
const starWars = process.argv[2];
let counter = 0;

axios.get(starWars).then(function (response) {
  for (let i = 0; i < response.data.results.length; i++) {
    for (let j = 1; j < response.data.results[i].characters.length; j++) {
      if (response.data.results[i].characters[j].includes('18')) {
        counter++;
      }
    }
  }
  console.log(counter);
});
