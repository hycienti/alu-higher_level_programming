#!/bin/bash
# This script sends a GET request and displays the body of the response for a 200 status code.
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -sL "$1"
