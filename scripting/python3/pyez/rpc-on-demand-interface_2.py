#!/usr/bin/env python3

from jnpr.junos import Device
from pprint import pprint
from lxml import etree

if __name__ == '__main__':
    dev = Device(host='srx210-1', user='dotel', passwd='junOS1314')
    dev.open()
    #pprint(dev.facts)	#checkpoint one

    interfaces_lxml_element = dev.rpc.get_interface_information(terse=True)
    #print(etree.tostring(route_lxml_element)) #checkpoint two
    #print(type(interfaces_lxml_element))

    list_of_inerfaces = interfaces_lxml_element.findall('.//physical-interface')
    #print(type(list_of_inerfaces))

    for interf in list_of_inerfaces:
        print("Interface: {} -- Status: {} -- IP: {}".format(interf.findtext('name').strip(), interf.findtext('oper-status').strip(), 
                                                      interf.findtext('logical-interface//ifa-local')))

    dev.close()


