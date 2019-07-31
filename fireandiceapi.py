#!/usr/bin/env python3 

import requests


HOUSES = "https://www.anapioficeandfire.com/api/houses?pagesize=2"

def fireicehouse():
    r = requests.get(HOUSES)
    return r.json()

def main():
    got = fireicehouse
    print(got)


main()

