#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header"""

if __name__ == "__main__":
    import requests
    import sys

    lis = sys.argv
    re = requests.get(lis[1])
    print(re.headers.get('X-Request-Id'))
