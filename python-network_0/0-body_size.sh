#!/bin/bash
# Fetches the size of the body of the response from a URL
curl -s -o /dev/null -w '%{size_download}' "$1"
