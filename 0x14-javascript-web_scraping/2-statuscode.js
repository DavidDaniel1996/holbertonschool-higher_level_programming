#!/usr/bin/node

const axios = require('axios');

function statusCode (response) {
  const code = response.status;
  console.log(`code: ${code}`);
}

function printError (err) {
  console.log(err);
}
axios.get(process.argv[2]).then(statusCode).catch(printError);
