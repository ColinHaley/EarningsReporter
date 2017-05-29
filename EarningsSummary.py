#!/usr/bin/env python

import sys, datetime
import argparse, logging, logging.handlers
import requests
import jinja2
from BeautifulSoup import BeautifulSoup
from Earnings import Earnings
from Logger import Logger
import smtplib
from email.mime.text import MIMEText
import ConfigParser

# Parse commandline args
parser = argparse.ArgumentParser(description="Earnings Whispers Web Scraper")
parser.add_argument("-l", "--logpath", help="Log file location.")
parser.add_argument("-d", "--days", help="Number of days to parse.")
parser.add_argument("-t", "--to", help="Email address to send summary to.")
parser.add_argument("-u","--backup_count", help="Number of log backups to keep.")
parser.add_argument("-x", "--disable_log", help="Do no logging.")

args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read('config/EarningsReporter.cfg')
target = config.get('Scraper', 'target')
# Might want to move into sub method with args as ... arg
if not args.disable_log:
    LOG_LEVEL = logging.INFO
    logger_setup()

if args.log:
    LOG_FILEPATH = args.log
else:
    LOG_FILEPATH = config.get('Logging', 'filepath')

if args.days:
    PARSE_DAYS = args.days
else:
    PARSE_DAYS = config.get('Scraper', 'days')

if args.rollover:
    LOG_ROLLOVER = args.rollover
else:
    LOG_ROLLOVER = config.get('Logging', 'rollover')

if args.backup_count:
    BACKUP_COUNT = args.backup_count
else:
    BACKUP_COUNT = config.get('Logging', 'backups')

# Logger object should be created either way in case of use.
# un _setup() loggers will only write to console.
logger = logging.getLogger(__name__)

def logger_setup(self):
    """docstring!"""

    #File log by script name
    logger.setLevel(LOG_LEVEL)

    # Keep 5 days rotate @ midnight
    handler = logging.handlers.TimedRotatingFileHandler(LOG_FILEPATH, when=LOG_ROLLOVER, backupCount=5)


    # standardize log format & attach to handler & to logger
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # redirect stdout and stderr to the logger
    sys.stdout = Logger(logger, logging.INFO)
    sys.stderr = Logger(logger, logging.ERROR)


if __name__ == '__main__':
    logger.info("__main__ called.")
    # In current method of running, only earnings whisper in epscalendar tag will
    # be aggregated. Anything under "morecalendar"" will not
    r = requests.get(target).content
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

def send_email(content):
    """send it home folks"""

