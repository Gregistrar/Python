#!/usr/bin/python3
"""

CoinMarketCap Developer Info - Need to create account for API key
https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide

Create web applets for notification triggers
https://ifttt.com/my_applets

Real Python Tutorial for Bitcoin Prices
https://realpython.com/python-bitcoin-ifttt/
"""

import pandas as pd
import numpy as np
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import time

bitcoin_price_threshold = 6000
bitcoin_api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/{}/with/key/cXOivYjv6Yive49ocVb6DU'

parameters = {'start': '1',
              'limit': '5000',
              'convert': 'USD'}
headers = {'Accepts': 'application/json',
           'X-CMC_PRO_API_KEY': '30f24f43-0cb5-4c51-8797-750f34e95ea5'}


def get_latest_bitcoin_price():
    session = Session()
    session.headers.update(headers)
    bitcoin_response = session.get(bitcoin_api_url, params=parameters)
    bitcoin_json = bitcoin_response.json()
    return float(bitcoin_json['data'][0]['quote']['USD']['price'])


def post_ifttt_webhook(event, value):
    data = {'value1': value}
    iftt_event_url = ifttt_webhook_url.format(event)
    requests.post(iftt_event_url, json=data)


def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        date = bitcoin_price['date'].strftime('%d/%m/%Y %H:%M')
        price = bitcoin_price['price']
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{} - $<b>{}</b>'.format(date, round(price,2))
        rows.append(row)
    return '<br>'.join(rows)


def main():
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()
        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        if price < bitcoin_price_threshold:
            post_ifttt_webhook('bitcoin_price_emergency', price)

        if len(bitcoin_history) == 6:
            post_ifttt_webhook('bitcoin_price_update', format_bitcoin_history(bitcoin_history))
            # bitcoin_history = []

        time.sleep(10 * 60)


if __name__ == '__main__':
    main()




