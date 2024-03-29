#!/usr/bin/python3
"""
    Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should
    return None.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """The recursive function that queries Reddit API"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]
        if after is not None:
            recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
