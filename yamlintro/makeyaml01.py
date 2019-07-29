#!/usr/bin/env python3

import yaml

def main ():
    #creates list   
    vcp = [{"service": "computer", "app": "nova"}, {"service": "network", "app": "newtron"}, {"service": "clock", "app": "cinder"}]

    #prints list
    print(vcp)

    #open file and produce yaml
    with open ("vcp.yaml", "w") as vcpyaml:

        #Yaml only does dump, not dumps
        
        yaml.dump(vcp, vcpyaml)

main()
