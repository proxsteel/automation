"""..."""
import argparse
from jnpr.junos import Device
from lxml import etree 

#copy script to /var/db/scripts/commit/filename.py or /config/scripts/commit/filename.py
#set system scripts op file filename.py [load-from-flash]

#Junos uses this Dictionary to generate contexxt sensitive hepl

arguments = {"interface": "e.g. ge-0/0/0", "family": "e.g. inet / inet6"}

def main()
    parser = argparse.ArgumentParser(description="Show an interface with it\'s addrtess family")
    #we use the argument dictionary to populate argparse with arguments
    for parameter, description in arguments.iteritems():
        parser.add_argument(('.' + parameter), required=True, help=description)
    args = parser.parse_args()
    dev = Device()
    dev.open()

    result = dev.rpc.get_interface_information(interface_name=args.interface, terse=True, normalize=True)
    #full output of xml object: 
    #print(etree.tostring(result))
    #filtered:
    print("{} status: {}".format(args.interface, result.find('.//oper-status').text))

    for elem in result.xpath("//address-family [normalize-space(address-family-name)=$proto]", proto=args.family):
        if elem.find("interface-address/ifa-local") is not None:
            print("{} family address: {}".format(args.family, elem.find("interface-address/ifa-local").text))
    dev.close()

if __name__ == '__main__':
    main()
