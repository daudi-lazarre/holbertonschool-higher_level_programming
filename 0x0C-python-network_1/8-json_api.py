#!/usr/bin/python3
"""How to post an email"""

import requests
import sys

q = sys.argv

if __name__ == "__main__":
    if len(q) <= 1:
        data = {"q": ""}
    elif len(q) > 1:
        data = {"q": sys.argv[1]}

    try:
        url = requests.post("http://0.0.0.0:5000/search_user", data)

        if url.json():
            print("[{}] {}".format(url.json().get("id"),
                                   url.json().get("name")))

        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
