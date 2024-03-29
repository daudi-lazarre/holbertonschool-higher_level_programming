#!/usr/bin/node
const argv = process.argv;
const URL = argv[2];
const file = argv[3];
const fs = require('fs');
const request = require('request');

request(URL, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) return console.log(err);
    });
  }
});
