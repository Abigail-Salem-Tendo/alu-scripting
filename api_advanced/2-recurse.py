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
    returns:
        kist: List the article titles
    """

    #initialize the list of not provided
    if hot_list is None:
        hot_list = []

    url = ""

    headers = {

    }

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
        )


        if response.status_code != 200:
            return None

        data = response.json()
        posts = data["data"]["children"]
        # if no posts found and this is the first page, return None
        if not posts and after is None:
            return None
        # add titles from the current page to our list
        for post in posts:
            hot_list.append(post["data"]["title"])

        next_after = data["data"]["after"]

        if next_after:
            return recurse(subreddit, hot_list, next_after)
        else:
            return hot_list
