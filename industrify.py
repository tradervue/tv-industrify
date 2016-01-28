import sys
import os; sys.path.append("./py-tradervue-api")
import datetime
from tradervue import Tradervue

# Enter Tradervue username and password here #################
username = ""
password = ""
##############################################################

# Create your own user-agent, with your username or email included
user_agent = "Industrify API sample (support@tradervue.com)"

# Modify this function to supply your desired industry tag for each symbol
def tag_for_symbol(symbol):
  symbol_map = {
    "AAPL": "electronics",
    "BBY":  "retail",
    "FB":   "internet",
    "GS":   "finance",
    "MSFT": "software",
    "NFLX": "catv",
    "SPY":  "index",
    "TSLA": "autos",
    "TWTR": "internet"
  }
  if symbol in symbol_map:
    return symbol_map[symbol]
  else:
    return None


tv = Tradervue(username, password, user_agent)

page_size = 100
offset = 0

while True:
  trades = tv.get_trades(startdate = datetime.date(2016, 1, 1), max_trades = page_size, offset = offset)
  for t in trades:
    tag = tag_for_symbol(t["symbol"])
    if tag != None:
      if "tags" in t:
        if not tag in t["tags"]:
          t["tags"].append(tag)
          tv.update_trade(t["id"], tags = t["tags"])
          print "added {} tag to {} trade (id: {})".format(tag, t["symbol"], t["id"])
      else:
        tv.update_trade(t["id"], tags = [tag])
        print "added {} tag to {} trade (id: {})".format(tag, t["symbol"], t["id"])
  if len(trades) < page_size:
    break
  offset += page_size
  
print "done"