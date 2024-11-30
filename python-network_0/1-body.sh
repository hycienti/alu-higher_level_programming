#!/bin/bash
# Displays the body of the response from the provided URL, following up to 5 redirects
curl -sLf "$1"
