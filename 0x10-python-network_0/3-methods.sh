#!/bin/bash
#a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print substr($0, index($0,$2))}'
