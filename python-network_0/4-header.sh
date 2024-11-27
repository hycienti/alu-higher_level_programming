#!/bin/bash
# Sends a GET request with a custom header and displays the body of the response 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
