#!/usr/bin/python3
"""Sends a search request to the Twitter API.

Display format: [<Tweet ID>] <Tweet text> by <Tweet owner name>

Usage: ./103-search_twitter.py <consumer key> <consumer secret> <search string>
  - Uses the application-only authenitcation flow.
"""
import sys
import base64
import requests


if __name__ == "__main__":
    # Get bearer token
    url = "https://api.twitter.com/oauth2/token"
    token = "{}:{}".format(sys.argv[1], sys.argv[2]).encode("ascii")
    token = base64.b64encode(token).decode("utf-8")
    headers = {
        "Authorization": "Basic {}".format(token),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    payload = {"grant_type": "client_credentials"}
    r = requests.post(url, headers=headers, data=payload)
    bearer = r.json().get("access_token")

    # Make search request
    url = "https://api.twitter.com/1.1/search/tweets.json"
    headers = {
        "Authorization": "Bearer {}".format(bearer)
    }
    params = {
        "q": sys.argv[3],
        "count": "5"
    }
    url = "https://api.twitter.com/1.1/search/tweets.json"
    tweets = requests.get(url, headers=headers, params=params)

    # Print matched tweets
    tweets = tweets.json().get("statuses")
    for t in tweets:
        tweet_id = t.get("id")
        tweet_text = t.get("text")
        tweet_author = t.get("user").get("name")
        print("[{}] {} by {}".format(tweet_id, tweet_text, tweet_author))
