#!/bin/bash
# Displays size of the body of the URL response

curl -s 0.0.0.0:5000 | wc -c
