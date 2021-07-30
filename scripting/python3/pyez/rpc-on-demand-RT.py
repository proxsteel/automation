#!/usr/bin/env python3

from jnpr.junos import Device
from pprint import pprint
from lxml import etree

if __name__ == '__main__':
    dev = Device(host='srx210-1', user='dotel', passwd='junOS1314')
    dev.open()
    #pprint(dev.facts)	#checkpoint one

    route_lxml_element = dev.rpc.get_route_information(table="inet.0")
    #print(etree.tostring(route_lxml_element)) #checkpoint two

    list_of_routes = route_lxml_element.findall('.//rt')
    
    for route in list_of_routes:
        print("Route: {} -- Protocol: {} -- NH {}".format(route.findtext('rt-destination').strip(), 
                 route.findtext('rt-entry/protocol-name').strip(),
                 route.findtext('rt-entry/nh/to')))

    dev.close()


