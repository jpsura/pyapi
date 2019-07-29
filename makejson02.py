#!/usr/bin/env python3
import json

def main():
    #list of dictionary
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "betelgeusian"}, \
            {"name": "Authur Dent", "species": "human"}]

    #changes our list into a JSON string
    jsonstring = json.dumps(hitchhikers)

    #retuens the class that made the object list
    print(type(hitchhikers))

    #returns the class that made the object string
    print(type(jsonstring))

    #prints teh first string
    print(jsonstring)

    #prints the first list
    print(hitchhikers[0])

    print(jsonstring[0])


main()
