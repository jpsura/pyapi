#!/usr/bin/env python3

import uuid

#simulate job id with uuid package
ticket = uuid.uuid1()

try:
    print("please type the config file to load")
    configfile = input("filename: ")
    with open(configfile, 'r') as configfileobj:
        switchconfig = configfileobj.read()

except:
    x = "error with obtaining config file info"
else:
    x = "File Found"
finally:
    with open("try04.log", "a") as zlog:
        print("\n\nWriting results of service to log file...")
        print(ticket, " - ", x, file=zlog)
