#!/usr/bin/python3

#import needed libraries
#from jnpr.junos import Device
#from lxml.etree import dump, _Element
#from sys import argv
from ncclient import manager

node = "192.168.0.11"
user = "dotel"
ncport = 830
passwd = "junOS1314"

with manager.connect(host=node, port=ncport, username=user, password=passwd, device_params={'name':'junos'}) as mngr:
    c = mngr.get_config(source='running').data_xml #running == active; candidate == canditate
    with open("%s.xml" % node, 'w') as f:
        print("Saving to {}.xml file".format(node))
        f.write(c)

