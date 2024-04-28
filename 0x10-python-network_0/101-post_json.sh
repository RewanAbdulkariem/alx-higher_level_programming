#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
json_data=$(cat "$2")
curl -s -H 'Content-Type: application/json' -d @"$2" -X POST "$1"
