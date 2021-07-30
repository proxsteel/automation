#!/usr/bin/env python3

from jnpr.junos import Device
from lxml import etree
from pprint import pprint

if __name__ == '__main__':
    with  Device(host='srx210-1', user='dotel', passwd='junOS1314', normalize=True) as dev:
        cnf = dev.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))
#, options={'format': 'jason'})
#        cnf = dev.rpc.get_config(filter_xml="configuration/interfaces")
#        pprint(etree.tostring(cnf))
        print(etree.tostring(cnf))
