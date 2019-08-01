#!/usr/bin/env python3

import requests
import alpha_vantage
from pprint import pprint

API_URL = "https://www.alphavantage.co/query"

data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "vz",
    "outputsize": "compact",
    "datatype": "json",
    "apikey": "NJTO68R6JE6UHSO0",
    }
response = requests.get(API_URL, data)
pprint(response.json())
