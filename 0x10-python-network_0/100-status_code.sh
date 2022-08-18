#!/bin/bash
# Display status code of response
curl -sI "$1" | grep HTTP | cut -d " " -f 2
 