#!/bin/bash
# Sends a GET request to a URL and displays the body if the response is 200
curl -s -o /dev/null -w '%{http_code}' "$1" | grep -q "^200$" && curl -s "$1"
