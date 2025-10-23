#!/usr/bin/python3
"""
A function the queries the Reddit API and prints the
title of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """
    Print the title of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {}
    queries = {"limit": 10}

    reponse = requests.get(url, params=queries, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            print(post["data"]["title"])
        return "OK"
    else:
        print(None)
        return "OK"
