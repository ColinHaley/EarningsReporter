#!/usr/bin/env python

import sys, datetime
import argparse
import requests
import jinja2
from BeautifulSoup import BeautifulSoup
from Earnings import Earnings
from Logger import Logger

today_earnings_whisper_url = "https://www.earningswhispers.com/calendar?sb=p&d={day}&t=all"


# Defaults
LOG_FILEPATH = "/tmp/EarningsSummary.log"
LOG_LEVEL = logging.info
PARSE_DAYS = 14

# Parse commandline args
parser = argparse.ArgumentParser(description="Earnings Whispers Web Scraper")
parser.add_argument("-l", "--log", help="Log file location. Default: {0}".format(LOG_FILEPATH))
parser.add_argument("-d", "--days", help="Number of days to parse. Default: {0}".format(PARSE_DAYS))

args = parser.parse_args()
if args.log:
    LOG_FILENAME = args.log
if args.days:
    PARSE_DAYS = args.days

#File log by script name
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# Keep 5 days rotate @ midnight
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=5)

# standardize log format & attach to handler & to logger
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# redirect stdout and stderr to the logger
sys.stdout = Logger(logger, logging.INFO)
sys.stderr = Logger(logger, logging.ERROR)


if __name__ == '__main__':
    init()
    # In current method of running, only earnings whisper in epscalendar tag will
    # be aggregated. Anything under "morecalendar"" will not
    r = requests.get(today_earnings_whisper_url).content
    soup = BeautifulSoup(r)
    earnings_data = []
    # eps calendar should always exist
    datasets = soup.findAll("ul", {"id":"epscalendar"})[0]

    lis=datasets.findAll("li")
    for li in lis:
        try:
            earnings_data.append(Earnings(li))
        except:
            pass

def init(self):
    """
    Initialize Logger and write out system stats and runtimes

    """
    logger.info("Initalize Called")

def send_email(content):
    #send it home folks

