import uuid

class Earnings(object):
    """An individual event parsed from https://www.earningswhispers.com/calendar?sb=p&d=1&t=all&v=t
    d = 0 is today. d++ for days
    Attributes:
        Confirmed: A Boolean representing confirmation of an earnings report.
        Company: A string representing Company Name
        Symbol: A string representing Ticker Symbol
        Last Confirmed: A string representing the time of the earnings report taking place.
        Estimated EPS: 
        Estimated Revenue:
    """
    def __init__(self, earnings_html):
        """parse html objects to variables
        
        This is absolutely going to need some optimization. findAll calls have lots of overhead.
        """
        self.id = uuid.uuid1()
        self.confirmed = earnings_html.findAll('div', {'class':'confirm icon-check'})
        self.company = earnings_html.findAll('div', {'class':'company'})
        self.ticker = earnings_html.findAll('div', {'class':'ticker'})
        self.time = earnings_html.findAll('div', {'class':'time'}) # earnings datetime
        self.estimated_eps = earnings_html.findAll('div', {'class':'estimate'}) # eps estimate
        self.estimated_revenue = earnings_html.findAll('div', {'class':'revestimate'}) #evenue estimate
#    __logo_base__ = "http://cdn.instantlogosearch.com/png?id=instantlogosearch-{0}"

    def gaga(self):
        print("Confirmed: {0}\n"+"Company: {1}\n")
