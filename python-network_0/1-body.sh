#!/bin/bash
# Fetch and display the body of a URL response with 200 status code
curl -s "$1" | grep -v "HTTP" | sed '/^$/d'
