#!/usr/bin/env python3
import urllib.request
import json

LIST = 'http://api.open-notify.org/astros.json'

def main():
    ## Call the webservice
    isslist = urllib.request.urlopen(LIST)

    ## put fileobject into helmet
    datalist = isslist.read()

    ## decode JSON to Python data structure
    jsonlist = json.loads(datalist.decode('utf-8'))

    ## display our Pythonic data
    #print("\n\nConverted Python data")
    #print(jsonlist)

    print("\n\nPeople in Space: ", jsonlist['people'][0]['name'])
    print("                 ", jsonlist['people'][1]['name'])
    print("                 ", jsonlist['people'][2]['name'])
    print("                 ", jsonlist['people'][3]['name'])
    #print(jsonlist)

main()    
