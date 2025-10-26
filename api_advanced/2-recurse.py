#!/usr/bin/python3
"""
Recursive function that queries the REDDIT API and
returns a list of all the hot articles of a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    This question queries the Reddit API to get the hot articles

    Args:
        subreddit (str): the subreddit to search
        hot_list (list): list with article titles
        after (str): Pagination

    Returns:
        list: List the article titles
    """

    # initialize the list of not provided
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
               "User-Agent": "python:RedditTask3:v1.0 (by /u/Mental_Meal_9515)"
    }
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return None

        data = response.json().get("data", {})
        children = data.get("children", [])
        for post in children:
            hot_list.append(post.get("data", {}).get("title"))

        after = data.get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
