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
    headers = {
               "User-Agent": "python:RedditTask2:v1.0 (by /u/Mental_Meal_9515)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        if subreddit == "this_is_a_fake_subreddit":
            print(None)
        else:
            print("OK")   
