#!/usr/bin/env python

import sys
from datetime import datetime, timedelta
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
parser.add_argument("-u", "--backup_count", help="Number of log backups to keep.")
parser.add_argument("-r", "--rollover", help="When to rollover logs.")
parser.add_argument("-x", "--disable_log", help="Do no logging.")

args = parser.parse_args()

config = ConfigParser.ConfigParser()
config.read('config/EarningsReporter.cfg')
target = config.get('Scraper', 'target')
# Might want to move into sub method with args as ... arg
if args.logpath:
    LOG_FILEPATH = args.log
else:
    LOG_FILEPATH = config.get('Logging', 'filepath')

if args.days:
    PARSE_DAYS = args.days
else:
    PARSE_DAYS = int(config.get('Scraper', 'days'))

# 0 index, keep 0 but make sure top range is inclusive
PARSE_DAYS += 1

if args.rollover:
    LOG_ROLLOVER = args.rollover
else:
    LOG_ROLLOVER = config.get('Logging', 'rollover')

if args.backup_count:
    BACKUP_COUNT = args.backup_count
else:
    BACKUP_COUNT = int(config.get('Logging', 'backups'))

# Logger object should be created either way in case of use.
# un _setup() loggers will only write to console.
logger = logging.getLogger(__name__)

def logger_setup():
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


def send_email(content):
    """Content will be an object formatted as such:
    {
        "mmddyyyy" :
        [
            Earnings1,
            Earnings2
        ],
        "mmddyyyy" :
        [
            Earnings1,
            Earnings2
        ]
    }
    
    """


if __name__ == '__main__':
    if not args.disable_log:
        LOG_LEVEL = logging.INFO
        logger_setup()
        logger.info("__main__ called.")
    
    earnings_data = {}

    for day in range(0, PARSE_DAYS):
        current_target = target.format(day=day)

        # In current method of running, only earnings whisper in epscalendar tag will
        # be aggregated. Anything under "morecalendar"" will not
        
        try:
            r = requests.get(current_target)
            content = r.content            
            logger.info("Succesfully Requested: {0}".format(current_target) )
        except:
            #todo, add individual except blocks per failure type.
            logger.critical("Unable to request {0}".format(current_target))
            logger.critical("Request Status: {0}".format(str(r)))
            sys.exit(1)
        try:
            soup = BeautifulSoup(content)
        except:
            logger.critical("Unable to create BeautifulSoup object from {0}".format(current_target))
        
        # eps calendar should always exist
        datasets = soup.findAll("ul", {"id":"epscalendar"})[0]

        target_date = datetime.strftime(datetime.now() + timedelta(days=day),"%m%d%Y")
        earnings_data[target_date] = []

        lis=datasets.findAll("li")
        logger.info("Parsing {0} html tags".format(len(lis)))
        for li in lis:
            try:
                earnings_data[target_date].append(Earnings(li))
            except:
                pass

