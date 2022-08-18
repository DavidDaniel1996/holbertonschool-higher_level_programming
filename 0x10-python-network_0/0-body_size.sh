#!/bin/bash
# Displays size of the body of the URL response

curl -s "$1" | wc -c
