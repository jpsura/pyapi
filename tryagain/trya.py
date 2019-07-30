#!/usr/bin/env python3
while True:
    try:
        # pull info from user
        name = input('enter file name')
        with open(name, 'w') as myfile:
            myfile.write('Woop woop\n')
    except:
        print("Error, try again")

    else:
        print("File created")
        break
