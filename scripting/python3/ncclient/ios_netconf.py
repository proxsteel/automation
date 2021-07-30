#! /urs/bin/python3

#import needed libraries
#from jnpr.junos import Device
#from lxml.etree import dump, _Element
#from sys import argv
from ncclient import manager

node = "192.168.0.99"
user = "dotel"
ncport = 22
passwd = "junOS1314"

with manager.connect(host=node, port=ncport, username=user, password=passwd, hostkey_verify=False) as m:
    c = m.get_config(source='running').data_xml
    with open("%s.xml" % node, 'w') as f:
        f.write(c)

