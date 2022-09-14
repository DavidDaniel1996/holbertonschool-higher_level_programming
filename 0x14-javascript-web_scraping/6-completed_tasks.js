#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url).then(function (response) {
  const tasksCompleted = {};
  let userID = 0;
  let count = 0;
  for (let i = 0; i < response.data.length; i++) {
    if (userID !== response.data[i].userId) {
      count = 0;
      userID = response.data[i].userId;
    }
    if (response.data[i].completed === true) {
      count++;
      tasksCompleted[userID] = count;
    }
  }
  console.log(tasksCompleted);
});
