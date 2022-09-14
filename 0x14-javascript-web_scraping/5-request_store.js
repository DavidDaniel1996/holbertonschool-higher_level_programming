#!/usr/bin/node

const fs = require('fs');
const axios = require('axios');
const url = process.argv[2];
const fileName = process.argv[3];

axios.get(url).then(function (response) {
  fs.writeFile(fileName, response.data, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
