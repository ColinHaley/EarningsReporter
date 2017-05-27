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
    earnings_data_even_cor = soup.findAll("li", {"class":"cor bmo showconf nwh"})
    earnings_data_even_cors = soup.findAll("li", {"class":"cors bmo showconf nwh"})
    earnings_data_even_cor_shownot = soup.findAll("li", {"class":"cor bmo shownotconf nwh"})
    earnings_data_even_cors_shownot = soup.findAll("li", {"class":"cors bmo shownotconf nwh"})




