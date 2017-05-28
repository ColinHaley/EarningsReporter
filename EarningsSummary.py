__author__ = "Colin Haley"

import logging, sys
from BeautifulSoup import BeautifulSoup
import requests
import jinja2
import Earnings

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
today_earnings_whisper_url = "https://www.earningswhispers.com/calendar?sb=p&d=7&t=all"

#todo: Query <li> under <ul class="epscalendar", ensure len(<li>) == len(earnings_classes)
earnings_classes = ["cor bmo showconf nwh", "cors bmo showconf nwh",
                    "cor bmo shownotconf nwh", "cors bmo shownotconf nwh"]

if __name__ == '__main__':
    r = requests.get(today_earnings_whisper_url).content
    soup = BeautifulSoup(r)
    earnings_data = []

    for subclass in earnings_classes:
        for item in soup.findAll("li", {"class": subclass}):
            test = Earnings(item)
            earnings_data.append(test)

    for thing in earnings_data:
        thing.gaga()


def send_email(content):
    #send it home folks

