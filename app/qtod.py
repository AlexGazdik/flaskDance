import requests


def getQuote():
    url = "http://quotes.rest/qod.json"
    result = requests.request("GET", url)
    quote = result.json()
    result = quote['contents']['quotes'][0]['quote']
    author = quote['contents']['quotes'][0]['author']
    return str(result) + ' -' + str(author)   