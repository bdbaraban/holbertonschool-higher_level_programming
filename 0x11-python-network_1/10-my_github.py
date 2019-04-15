#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get("https://api.github.com/users/{}".format(sys.argv[1]))
    print(r.json().get("id"))
