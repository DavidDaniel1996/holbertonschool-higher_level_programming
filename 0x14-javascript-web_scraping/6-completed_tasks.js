#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url).then(function (response) {
  const tasksCompleted = {};
  let userID = 0;
  let count = 0;
  for (let i = 0; i < response.data.length; i++) {
    userID = response.data[i].userId;
    if (!(userID in tasksCompleted)) {
      count = 0;
    }
    if (response.data[i].completed === true) {
      count++;
      tasksCompleted[userID] = count;
    }
  }
  console.log(tasksCompleted);
}).catch(err => {
  console.log(err);
  return (err);
});
