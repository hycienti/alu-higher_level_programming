#!/bin/bash 
# takes in a url and display the content length 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
