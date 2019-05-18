# Python - Network #1

This project involved learning how to use the `urllib` and `requests` Python
libraries to send and receive HTTP messages to URL's. I practiced sending `GET`
and `POST` requests, fetching JSON resources, and interacting with API's (the
Star Wars API, GitHub API, and Twitter API).

## Tasks :page_with_curl:

* **0. What's my status? #0**
  * [0-hbtn_status.py](./0-hbtn_status.py): Python script that fetches
  `https://intranet.hbtn.io/status`.
  * Uses `urllib`.

* **1. Response header value #0**
  * [1-hbtn_header.py](./1-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./1-hbtn_header.py <URL>`
	* Uses `urllib`.

* **2. POST an email #0**
  * [2-post_email.py](./2-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./2-post_email.py <URL> <email>`.
	* Uses `urllib`.

* **3. Error code #0**
  * [3-error_code.py](./3-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `urllib`.

* **4. What's my status? #1**
  * [4-hbtn_status.py](./4-hbtn_status.py): Python script that fetches
  `https://intranet.hbtn.io/status`.
  * Uses `requests`.

* **5. Response header value #1**
  * [5-hbtn_header.py](./5-hbtn_header.py): Python script that displays the
  `X-Request-Id` response header variable of a request to a given URL.
  * Usage: `./5-hbtn_header.py <URL>`
	* Uses `requests`.

* **6. POST an email #1**
  * [6-post_email.py](./6-post_email.py): Python script that sends a `POST`
  request to a given URL with a given email, and displays the response body.
  * Usage: `./6-post_email.py <URL> <email>`.
	* Uses `requests`.

* **7. Error code #1**
  * [7-error_code.py](./7-error_code.py): Python script sends a request to
  a given URL and displays the response body.
  * Handles HTTP errors.
	* Uses `requests`.

* **8. Search API**
  * [8-json_api.py](./8-json_api.py): Python script that sends a `POST` request
  to `http://0.0.0.0:5000/search_user` with a letter passed as parameter.
  * Usage: `./8-json_api.py <letter>`
	* The letter is sent as the value of the variable `q`.
	* If no letter is given, sets `q=""`.
	* If the response body is properly formatted and non-empty, displays it as
  `[<id>] <name>`.
  * Uses `requests`.

* **9. Star Wars API #0**
  * [9-starwars.py](./9-starwars.py): Python script sends a search request to
  the Star Wars API `people` endpoint with a given string.
  * Usage: `./9-starwars.py <search string>`
	* Displays the total number and `name` of each result.
	* Uses `requests`.

* **10. My Github!**
  * [10-my_github.py](./10-my_github.py): Python script that takes GitHub
  credentials (username and password) and uses the Github API to display the
  corresponding ID.
  * Usage: `./10-my_github.py <username> <password>`
	* Uses `requests`.

* **11. Time for an interview!**
  * [100-github_commits.py](./100-github_commits.py): Python script that lists
  the 10 most recent comments of a given GitHub repository using the GitHub API.
  * Usage: `./100-github_commits.py <repository name> <owner name>`
	* Uses `requests`.

* **12. Star Wars API #1**
  * [101-starwars.py](./101-starwars.py): Python script that sends a search
  request to the Star Wars API `people` endpoint with a given string.
  * Usage: `./101-starwars.py <search string>`
	* Displays the total number and `name` of each result.
	* Manages pagination to display all results.
	* Uses `requests`.

* **13. Star Wars API #2**
  * [102-starwars.py](./102-starwars.py): Python script that sends a search
  request to the Star Wars API `people` endpoint with a given string.
  * Usage: `./102-starwars.py <search string>`
	* Displays the total number and `name` of each result as well as the list of
  films associated with each character.
	* Manages pagination to display all results.
	* Uses `requests`.

* **14. Twitter Auth**
  * [103-search_twitter.py](./103-search_twitter.py): Python script that sends
  a search request to the Twitter API `search` endpoint with a given string.
  * Usage: `./103-search_twitter.py <consumer key> <consumer secret> <search string>`
	* Displays the the top 5 results in the format
  `[<Tweet ID>] <Tweet text> by <Tweet owner name>`.
  * Uses `requests`.
