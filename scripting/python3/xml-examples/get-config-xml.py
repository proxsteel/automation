#!/usr/bin/env python3

#import needed libraries
from jnpr.junos import Device
from lxml.etree import dump, _Element
from sys import argv

#use 1st command-line parameter as XPath, or use "." if it is not provided
#conf_xpath = "system/name-server/name" 

#Device credentials
USER = "dotel"
PASSWD = "junOS1314"
DEVICE_IP = "192.168.0.11"

#Open NETCONF connection with PyEZ Device class
with Device(host=DEVICE_IP, user=USER, password=PASSWD) as node:
    #Read a complete config using <get-config> RPC
    full_config = node.rpc.get_config()
    #filter the config with provided XPath
    filtered_config = full_config.xpath('.')
    #the result of applying XPath is a list - perform each loop
    for entry in filtered_config:
       #for each entry, print() element or dump() if entry is _Element, _Element is eq <element></element>
       if type(entry) is _Element:
          dump(entry)
       else:
	#print the atribute
          print("the atribute is:",entry)
