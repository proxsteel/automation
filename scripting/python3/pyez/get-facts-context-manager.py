#!/usr/bin/env python3

from jnpr.junos import Device
from pprint import pprint
from lxml import etree

if __name__ == '__main__':
    with Device(host='srx210-2', user='dotel',passwd='junOS1314') as dev: #format is JSON by default. see format=text
        pprint(dev.facts)
        print('B'*100)
        sw_info_text = dev.rpc.get_software_information({'format':'text'}) #specify the format of RPC-replay xml/text/json
        print(etree.tostring(sw_info_text))  

#NOTE: dev.open() and dev.close() is not necesar since context manager will do that automatically.
