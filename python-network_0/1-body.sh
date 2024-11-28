#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of
# the response only if the status code is 200.

curl -sL -w "%{http_code}" "$1" -o temp_body | {
    read status
    if [ "$status" -eq 200 ]; then
        cat temp_body
    fi
    rm -f temp_body
}
