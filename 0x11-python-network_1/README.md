# 0x11. Python - Network #1

This repository contains Python scripts that demonstrate various network-related tasks using the urllib and requests libraries. Each script corresponds to a specific task aimed at fetching resources from the internet, sending HTTP requests, and interacting with web APIs.
## Files

-    0-hbtn_status.py: Fetches and displays the status of a specific URL using urllib.
-    1-hbtn_header.py: Retrieves the value of the X-Request-Id header from a URL using urllib.
-    2-post_email.py: Sends a POST request with an email parameter to a URL using urllib.
-    3-error_code.py: Handles HTTP errors and displays the error code for a given URL using urllib.
-    4-hbtn_status.py: Fetches and displays the status of a specific URL using requests.
-    5-hbtn_header.py: Retrieves the value of the X-Request-Id header from a URL using requests.
-    6-post_email.py: Sends a POST request with an email parameter to a URL using requests.
-    7-error_code.py: Handles HTTP errors and displays the error code for a given URL using requests.
-    8-json_api.py: Sends a POST request with a letter parameter to search for a user using requests and handles JSON responses.
-    10-my_github.py: Uses GitHub API with Basic Authentication to display the user ID using requests.

## Requirements

-    All scripts are written in Python 3.8.5 and must use the specified libraries (urllib or requests).
-    Scripts should be executable and adhere to PEP8 style guidelines using pycodestyle.
-    Each script must include a shebang (#!/usr/bin/python3) and appropriate documentation.
-    Use python3 -c 'print(__import__("my_module").__doc__)' to view documentation for each module.
-    Ensure code is executed only when run as a standalone script (if __name__ == "__main__":).

## Usage

To run these scripts, execute them from the command line with appropriate arguments:

```bash

./script_name.py [arguments]
```
For example:

```bash

./0-hbtn_status.py
./1-hbtn_header.py https://alx-intranet.hbtn.io
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
...
```