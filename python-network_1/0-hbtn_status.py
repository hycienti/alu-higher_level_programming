#!/usr/bin/python3
"""
This script fetches a URL using urllib and displays the body of the response.
The default URL is https://alu-intranet.hbtn.io/status,
but you can pass a different URL as an argument during script invocation.
"""

from urllib import request
import sys

if __name__ == "__main__":
    # Set default URL
    url = 'https://alu-intranet.hbtn.io/status'
    
    # If a URL is passed as an argument, use it instead of the default
    if len(sys.argv) > 1:
        url = sys.argv[1]
    
    # Fetch the URL
    with request.urlopen(url) as response:
        body = response.read()

    # Print the output in the specified format
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
