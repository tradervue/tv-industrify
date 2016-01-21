Industrify - Tradervue API Sample Application
=============================================

This is a simple Python application that uses the [Tradervue API](https://github.com/tradervue/api-docs)
to add industry tags to existing trades in Tradervue. Only a few symbols are mapped with industry
tags, but you can easily modify the script to use any tag you need for any symbol.

This script uses [py-tradervue-api](https://github.com/nall/py-tradervue-api), a Python 
API wrapper developed by [@nall](https://github.com/nall).

To install the script and its dependencies (assuming you already have Python installed):

```
# first clone this repository
git clone https://github.com/tradervue/tv-industrify.git

# change into this repo's folder
cd tv-industrify

# clone py-tradervue-api as a subfolder
git clone https://github.com/nall/py-tradervue-api.git
```

Then open industrify.py, and edit the script as follows:

- add your Tradervue username and password
- add a new user-agent that includes your Tradervue username or email (if you're planning to use the script
  for more than just testing)
- edit the mapping from symbols to tags, for whatever symbols/tags you need (or provide a different
  lookup mechanism for these)
- by default, the script will only modify 100 trades maximum, and only trades opened on 
  or after 1/1/2016. You can change either of these parameters in the get_trades call to meet your needs.

Then run the script with python:

`python industrify.py`

Note that this API sample isn't intended to show best practices - it's just a simple example of an app that uses
the Tradervue API to add tags to trades.
