#!/usr/bin/env python3

def main():
    jlist = ['cisco', 'juniper', 'bigip', 'tellabs', 'meraki']

    print(jlist[2])

    jlist.append('alcatel')
    
    print(jlist[5])

    jcloud = ['aws', 'openstack', 'google']

    jlist.extend(jcloud)

    print(jlist)


main()

