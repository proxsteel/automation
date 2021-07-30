#!/usr/bin/python3

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *

#print("packeges are imported sucessfully.")

if __name__ == '__main__':
    try:
        dev = Device(host='srx210-1', user='dotel', passwd='junOS1314')
        dev.open()

        conf = Config(dev)
        conf.lock()
        conf.load(path="bgp-config.conf", merge=True, format='text')
        conf.pdiff()
        if conf.commit_check():
            conf.commit(comment='Updating BGP config')
            print("Configuration applied!")
        else:
            conf.rollback()
            print("Rolling back...")

        conf.unlock()
        print("Configuration unlocked!")

    except ConnectAuthError:
        print("Authentication Error arised!")
    except ConnectTimeoutError:
        print("NETCONF Connection timeout!")
    except ConnectError as error:
        print("Undetermined connection error: {}".format(error))
    except ConfigLoadError as error: 
        print("Can\'t load the configuration...\n --> {}".format(error))
    except Exception as error:
        print("Another exception arised: {}".format(error))
    finally:
        dev.close()
