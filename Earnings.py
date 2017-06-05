import uuid
from json import JSONEncoder

class Earnings(object):
    """An individual event parsed from https://www.earningswhispers.com/calendar?sb=p&d=1&t=all&v=t
    d = 0 is today. d++ for days
    Attributes:
        Confirmed: A string representing confirmation of an earnings report.
        Company: A string representing Company Name
        Symbol: A string representing Ticker Symbol
        Last Confirmed: A string representing the time of the earnings report taking place.
        Estimated EPS: 
        Estimated Revenue:
    """
#   Todo, parse logo + company minutes
#   __logo_base__ = "http://cdn.instantlogosearch.com/png?id=instantlogosearch-{0}"

    def __init__(self, earnings_html):
        """parse html objects to variables
        
        This is absolutely going to need some optimization. findAll calls have lots of overhead.
        """
        self.id = uuid.uuid1()
        try:
            confirm_date = earnings_html.findAll("div", {"class":"confirm icon-check"})[0]['title']
            if (len(confirm_date) >= 1):
                self.confirmed = confirm_date
            else:
                self.confirmed = "Unconfirmed"
        except:
            self.confirmed = "Unconfirmed"
        try:
            self.company = earnings_html.findAll('div', {'class':'company'})[0].text
        except:
            self.company = "Unspecified"
        try:
            self.ticker = earnings_html.findAll('div', {'class':'ticker'})[0].text
        except:
            self.ticker = "Unspecified"
        try:
            self.time = earnings_html.findAll("div", {"class":"time"})[0].text # earnings datetime
        except:
            self.time = "Unspecified"
        try:
            self.estimated_eps = earnings_html.findAll('div', {'class':'estimate'})[0].text # eps estimate
        except:
            self.estimated_eps = "Unspecified"
        try:
            self.estimated_revenue = earnings_html.findAll('div', {'class':'revestimate'})[0].text #evenue estimate
        except:
            self.estimated_revenue = "Unspecified"


    def debug_print(self):
        print("Confirmed: {0}\nTicker: {1}\nCompany: {2}\nTime: {3}\nEstimated EPS: {4}\nEstimated Revenue: {5}\n---\n"
        .format(self.confirmed, self.ticker, self.company, self.time, self.estimated_eps, self.estimated_revenue))

#    def to_json(self):
#         return {"do":"some","json":"magics"}