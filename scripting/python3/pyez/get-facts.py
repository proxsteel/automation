#!/usr/bin/env python3

from jnpr.junos import Device
from pprint import pprint

if __name__ == '__main__':
    
    dev = Device(host='srx210-1', user='dotel', passwd='junOS1314') #get_facts=False may reduce exce time 
    dev.open()
    pprint(dev.facts['hostname']) #or ['RE0']['up_time']
    dev.close()
#facts is a nested dictionary
