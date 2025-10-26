#!/usr/bin/python3
"""
This function creates a request to get the
number of subcribers from the reddit api.
"""
import requests


def number_of_subscribers(subreddit):
    """
    return the muber of subcribers of a subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {}
    response = requests.get(url, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
