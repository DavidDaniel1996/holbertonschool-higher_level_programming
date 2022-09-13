#!/usr/bin/node

const fs = require('fs');

function readData (data) {
    try {
        console.log(data);
    }
    catch(err) {
        console.log(err.message);
    }
};

fs.readFile(process.argv[2], 'utf-8', readData);
