#!/usr/bin/python3
"""script that takes your Github credentials"""

if __name__ == '__main__':
    import requests
    import sys

    headers = {}
    headers['Authorization'] = '{} {}'.format(sys.argv[0], sys.argv[1])
    r = requests.get('https://api.github.com/users/{}'
                     .format(sys.argv[1]), headers=headers)
    print(r.json().get('id'))
