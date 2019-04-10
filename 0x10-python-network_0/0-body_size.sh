#!/usr/bin/env bash
# Usage: ./0-body_size.sh <URL>
# Sends a GET request to the given URL and displays
#+ the byte size of the response body.

curl -s "$1" | wc -c
