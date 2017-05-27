__author__ = "Colin Haley"

import logging, sys
from BeautifulSoup import BeautifulSoup
import requests
import jinja2

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
today_earnings_whisper_url = "https://www.earningswhispers.com/calendar?sb=p&d=0&t=all"

def send_email(content):
    #send it home folks


if __name__ == "__main__":
    r = requests.get(today_earnings_whisper_url).content
    soup = BeautifulSoup(r)
    earnings_data = soup.findAll("li", {"class":"cor bmo showconf nwh"})




