__author__ = "Colin Haley"

import logging, sys
from BeautifulSoup import BeautifulSoup
import requests

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
today_earnings_whisper_url = "https://www.earningswhispers.com/calendar?sb=p&d=0&t=all"

if __name__ == "__main__":
    r = requests.get(today_earnings_whisper_url)


