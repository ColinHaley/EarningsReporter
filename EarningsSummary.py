__author__ = "Colin Haley"

import logging, sys
from BeautifulSoup import BeautifulSoup
import requests
import jinja2
from Earnings import Earnings

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
today_earnings_whisper_url = "https://www.earningswhispers.com/calendar?sb=p&d=7&t=all"

#todo: Query <li> under <ul class="epscalendar", ensure len(<li>) == len(earnings_classes)

if __name__ == '__main__':
    r = requests.get(today_earnings_whisper_url).content
    soup = BeautifulSoup(r)
    earnings_data = []
    # eps calendar should always exist
    datasets = soup.findAll("ul", {"id":"epscalendar"})[0]

    lis=datasets.findAll("li")
    for li in lis:
        try:
            earnings_data.append(Earnings(li))
            #li.findAll("div",{"class":"ticker"})[0].text
        except:
            pass
            

    for thing in earnings_data:
        thing.gaga()


def send_email(content):
    #send it home folks

