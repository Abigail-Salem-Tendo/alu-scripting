#!/usr/bin/python3
"""
This function creates a request to get the number of subcribers from the reddit api.
"""


import requests


def number_of_subcribers(subreddit):
    url = "https://www.reddit.com/dev/api/{}".format(subreddit)
    headers = {
