#!/usr/bin/env python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

if __name__ == '__main__':
    dev = Device(host='ex3200-1', user='netonf', passwd='junOS1314')

    dev.open()
    conf = Config(dev)

    data = """set system services rest http
    set system services rest http port 3030
    """

    conf.lock()
    conf.load(data, format='set')
    conf.pdiff()
    
    if conf.commit_check(): #if true then commit
        conf.commit()
    else:
        conf.rollback()

    conf.unlock()
    dev.close()

