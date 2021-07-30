#!/usr/bin/env python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from lxml import etree

if __name__ == '__main__':

    data = 'set system services netconf traceoptions file netconf.log'

    with Device(host='srx210-2', user='netconf', passwd='junOS1314') as dev:
        #active_cnf = dev.rpc.get_config(filter_xml=etree.XML('<configuration><system><services><netconf></netconf></services></system></configuration>'))
        #print(etree.tostring(active_cnf))
        with Config(dev, mode="exclusive") as conf:
            #conf.lock()
            conf.load(data, format='set')
            #conf.pdiff()
            diff = conf.diff()
            if diff is None: #if no changes then do nothing "is eq =="
                print("The configuration already up to date!")
            else:
                print(diff)
                if conf.commit_check():
                    print("Commiting changes now!")
                    conf.commit(comment='Configuring netconf traceoptions')
                else:
                    conf.rollback()   
