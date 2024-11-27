#!/usr/bin/python3
"""
This module fetches the status from https://alu-intranet.hbtn.io/status using urllib
and displays the response details in the specified format.
"""
import urllib.request


def fetch_hbtn_status():
    """
    Fetch and display the status from the specified URL.
    
    Uses urllib to open the URL and prints response details 
    including type, content, and UTF-8 decoded content.
    """
    url = "https://alu-intranet.hbtn.io/status"
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_hbtn_status()
