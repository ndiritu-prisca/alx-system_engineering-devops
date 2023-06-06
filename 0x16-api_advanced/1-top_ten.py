#!/usr/bin/python3
"""
    A function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """The function that queries the Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("None")
        return
