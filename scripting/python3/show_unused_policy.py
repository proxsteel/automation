#!/usr/bin/env python3

from lxml import etree

CONF_FILENAME = "device_config.xml"

if __name__ == "__main__":

    config = etree.parse(CONF_FILENAME).getroot()

    policies_configured_list = config.xpath("policy-options/policy-statement/name")

    policies_configured_set = set()

    for element in policies_configured_list:
        policies_configured_set.add(element.text)
    
    print("Policies configured globaly ", policies_configured_set, "\n")

    policies_used_list = config.xpath("protocols//import") + \
                         config.xpath("protocols//export")
    
    policies_used_set = set()

    for element in policies_used_list:
        policies_used_set.add(element.text)
    
    print("Policies configured in routing protocols: ", policies_used_set, "\n")

    policies_unused_set = policies_configured_set - policies_used_set

    print("Unused Policies are: ", policies_unused_set)
