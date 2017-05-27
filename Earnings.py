class Earnings(object):
    """An individual event parsed from https://www.earningswhispers.com/calendar?sb=p&d=1&t=all&v=t
    
    d = 0 is today. ++ or -- for prior and current days

    Attributes [prefix of # indicates typically only populated for prior days]:
        Symbol: A string representing Ticker Symbol
        Company: A string representing Company Name
        Confirmed: A Boolean representing confirmation of an earnings report.
        #Last Confirmed: A string representing the time of the earnings report taking place.
        Estimated EPS: 
        Estimated Revenue:
        #Reported EPS:
        #Reported Revenue:
        #ESP Surprise %:
        #Revenue Surprise %:
        #Earnings Growth
        #Revenue Growth

    """

    __logo_base__ = "http://cdn.instantlogosearch.com/png?id=instantlogosearch-{0}"

def parse_html(soup_object):
    """parse html objects to variables
    
    This is absolutely going to need some optimization. 
    """

    soup_object.findAll('div',{'class':'confirm icon-check'})
    soup_object.findAll('div',{'class':'company'})
    soup_object.findAll('div',{'class':'ticker'})
    soup_object.findAll('div',{'class':'actestimate'}) #reported eps
    soup_object.findAll('div',{'class':'time'} # earnings datetime
    soup_object.findAll('div',{'class':'estimate'}) # eps estimate
    soup_object.findAll('div',{'class':'revestimate'}) #evenue estimate
    

def __init__(self, earnings_html):
    parse_html(earnings_html)

#def lookup_logo(self):
    # lookup logo using 


