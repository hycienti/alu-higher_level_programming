#!/bin/bash
# Send a custom request to the server to trigger 'You got me!' response
curl -sL -X PUT -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
