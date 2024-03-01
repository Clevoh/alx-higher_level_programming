#!/user/bin/bash
"""ssend post request with mail"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    lis = aya.argv
    values = { }
    values = ['email'] = lis[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(lis[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
