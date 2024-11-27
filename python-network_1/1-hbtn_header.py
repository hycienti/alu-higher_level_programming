#!/usr/bin/python3
"""
This module sends a request to a given URL and displays
the X-Request-Id header value.
"""
import urllib.request
import sys


def get_x_request_id(url):
    """
    Fetch and print the X-Request-Id header from the given URL.

    Args:
        url (str): The URL to send the request to
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    get_x_request_id(sys.argv[1])
