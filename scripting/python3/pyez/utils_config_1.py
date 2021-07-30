#!/usr/bin/env python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

if __name__ == '__main__':
    dev = Device(host='srx210-2', user='dotel', passwd='junOS1314')

    dev.open()
    conf = Config(dev)

    data = """interfaces {
        ge-0/0/1 {
            unit 0 {
                family inet {
                    address 188.20.1.160/24;
                }
            }
        }
    }"""

    conf.lock()
    conf.load(data, format='text')
    conf.pdiff()
    
    if conf.commit_check(): #if true then commit
        conf.commit()
    else:
        conf.rollback()

    conf.unlock()
    dev.close()
