#!/usr/bin/env python3

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

PACKAGE = 'var/tmp/junos-openconfig-18.tgz' #openconfig pkg doesnt require reboot

def myprogress(dev, report):
    print "host: %s, report: %s" % (dev.hostname, report)

if __name__ == '__main__':
    dev = Device(host='srx210-1', user='netonf', passwd='junOS1314')
    dev.open()

    sw = SW(dev)

    sw_upgrd = sw.install(package=PACKAGE, no_copy=True, validate=False, progress=myprogress)
#   sw.reboot() 
    dev.close()

#Note: sw.install() does not perform a reboot, use sw.reboot() if needed.
"""Primary methods:
   -  install(): perform the entire software installation process
   -  reboot(): reboots the system for the new image to take effect
   -  poweroff(): shutdown the system
  
   Helpers: (Useful as standalone as well)
   -  put(): SCP put package file onto Junos device
   -  pkgadd(): performs the ‘request’ operation to install the package
   -  validate(): performs the ‘request’ to validate the package
   
  Miscellaneous:
   -  rollback: same as ‘request software rollback’
   - inventory: (property) provides file info for current and rollback images on the devic
"""
