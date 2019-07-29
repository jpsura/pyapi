#!/usr/bin/python3

def main():
    hostipdict = {"host01": "10.0.0.2", "host2": "10.2.3.4", "host3": "10.3.4.5"}

    print(hostipdict['host2'])

    hostipdict['host4'] = '172.0.0.1'

    print(hostipdict)

    hostipdict.update({'host5': '10.3.2.4'})

    print(hostipdict)

    print(hostipdict.get('host66'))

    print(hostipdict.keys())

    print(hostipdict.values())


main() 
