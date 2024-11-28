#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
