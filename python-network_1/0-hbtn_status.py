#!/usr/bin/python3
"""
This script fetches a status URL using the urllib package and displays the response.
It handles both `https://alu-intranet.hbtn.io/status` and `http://0.0.0.0:5050/status`.
"""

import urllib.request

if __name__ == "__main__":
    urls = ["https://alu-intranet.hbtn.io/status", "http://0.0.0.0:5050/status"]
    content = None

    # Try fetching from both URLs, prioritizing the first one.
    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                content = response.read()
                break  # Exit loop if successful
        except Exception as e:
            continue

    if content:
        # Printing the output in the required format
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
    else:
        print("Failed to fetch the status from both URLs.")
