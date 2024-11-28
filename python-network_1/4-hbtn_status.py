#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status using the
requests package and displays the response body in a specific format.
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
