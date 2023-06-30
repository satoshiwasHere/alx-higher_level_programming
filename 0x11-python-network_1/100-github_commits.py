#!/usr/bin/python3
"""
Python script takes 2 arguments in order to solve a challenge
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)

    req = requests.get(url)
    comm = request.json()

    try:
        for x in range(10):
            print('{}: {}'.format(
                comm[x].get('sha'),
                comm[x].get('commit').get('author').get('name')))
    except IndexError:
        pass
