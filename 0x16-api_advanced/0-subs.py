#!/usr/bin/python3
"""
    A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given
    subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """A method that returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Custom User Agent'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        return 0
