#!/usr/bin/node

const axios = require('axios');

function statusCode (response) {
  const code = response.status;
  console.log(`code: ${code}`);
}

function printError () {
  console.log('code: 404');
}
axios.get(process.argv[2]).then(statusCode).catch(printError);
