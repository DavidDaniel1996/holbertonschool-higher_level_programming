#!/usr/bin/node

const axios = require('axios');

function statusCode (response) {
  const code = response.status;
  console.log(`code: ${code}`);
}

function printError (error) {
    const code = error.response.status
    console.log(`code: ${code}`)
}
axios.get(process.argv[2]).then(statusCode).catch(printError);
