#!/bin/bash
# Send a POST request with JSON contents from a file and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
