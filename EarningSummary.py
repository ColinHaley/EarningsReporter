class Test(earnings_html,self):
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
