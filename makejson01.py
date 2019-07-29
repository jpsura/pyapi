#!/usr/bin/env python3
import json

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "betelgeusian"}, \
            {"name": "Authur Dent", "species": "human"}]

    print(hitchhikers)

    with open("galaxyguide.json", "w") as jfile:
        json.dump(hitchhikers, jfile)


main()
