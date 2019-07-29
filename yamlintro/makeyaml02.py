#!/usr/bin/env python3

import yaml
import json

def main ():

    #open file and produce yaml
    with open ("vcp.yaml", "r") as vcp:
        pyyammy = yaml.load(vcp)
    pyyammy.append({"service": "Identity", "app": "keystone"})    

    print(pyyammy)

    with open ("vcp.json", "w") as vcpjson:
        json.dump(pyyammy, vcpjson)


main()
