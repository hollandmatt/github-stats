# GitHub stats reader

A script to read pull request statistics from the GitHub API, and write them to a CSV file for import into BI tools/Excel/etc.

## Usage

1. Install Python - `brew install python` on a Mac
1. Install the requests module - `pip install requests` or `easy_install requests`
1. Copy `config.template.json` to `config.json` and add (All of these are required):
  1. `token`: your GitHub OAuth token
  1. `repos`: repositories you're interested in. The user who created your token must have access to the repo if they are private.
  1. `output`: path you want the output written to
1. `./pull_requests.py`
1. Results are in the filename you specified
