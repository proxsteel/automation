#!/usr/bin/env python3
from lxml import etree
import pprint
    
with open('./srx.interfaces.xml') as fh:
    interfaces_xml = etree.fromstring(fh.read())
    
def node_values_list(xml_doc, xpath_expr):
    return [ x.text for x in xml_doc.xpath(xpath_expr) ]
    
# Example Paths
xpath_all_nodes = '//name'    # starting '//' means find the subsequent path anywhere in the document
xpath_absolute = '/rpc-reply/interface-information/physical-interface/name'  # starting '/' means anchor at root
#Or xpath_absolute = './interface-information/physical-interface/name'  # starting './' means anchor at root which is /rpc-replay

# Example Predicates:
xpath_starts_with = '/rpc-reply/interface-information/logical-interface[starts-with(name, "lo")]/name'
xpath_match = '/rpc-reply/interface-information/physical-interface[oper-status = "up"]/name'
xpath_not_match = '/rpc-reply/interface-information/physical-interface[oper-status != "up"]/name'
xpath_position = '/rpc-reply/interface-information/physical-interface[3]/name'
xpath_reverse_position = '/rpc-reply/interface-information/physical-interface[last()-1]/name'

""" NOTE: Predicates are used to find nodes that have specific values. The match conditions in predicates are specified between square brackets. 
          Using predicates we can filter output further. By plugging in different expressions to our function we can see how they affect the data that is returned:"""

print("All Nodes: ", node_values_list(interfaces_xml, xpath_all_nodes))

print("Absolute XPath", node_values_list(interfaces_xml, xpath_absolute))

print("Reverse pozition", node_values_list(interfaces_xml, xpath_reverse_position))
