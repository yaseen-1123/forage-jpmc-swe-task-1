
import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    """ ------------- Update this function ------------- """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = bid_price
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    return 1


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        """ ----------- Update to get the ratio --------------- """
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))

        print("Ratio %s" % getRatio(price, price))
def getDataPoint(quote):
    """Produce all of the needed values to generate a datapoint"""
    """_____________Update this function________"""
    stock=quote['stock']
    bid_price=float(quote['top_bid']['price'])
    ask_price=float(quote['top_bid']['price'])
    price= (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b"""
    """____________Update this function ______"""
    """Also create some unit test for this function in client_test.py"""
    if (price_b==0):
        return
    return price_a/price_b

# main
if __name__== "__mian__":
    # Quarrey the price once evry n seconds
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.Random())).read())

        """___________update to get the ratio_____________"""
        price = {}
        for quote in quotes:
            stock, bid_price, ask_price, price=getDataPoint(quote)
            price[stock]=price
            print(" Quated %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price ))

        print("Ratio %s" % getRatio(price["ABC"], price ["DEF"]))
