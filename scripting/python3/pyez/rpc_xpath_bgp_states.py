#!/usr/bin/env python3

from jnpr.junos import Device

if __name__ == '__main__':
    #define colector variables
    peers_established = 0
    peers_other = 0
    
    dev = Device(host='srx210-1', passwd='junOS1314')
    dev.open()
    
    bgp_data = dev.rpc.get_bgp_summary_information()
    neighbor_states = bgp_data.xpath("bgp-peer/peer-state")

    for state in neighbor_states:
        if state.text == "Established":
            peers_established += 1
        else:
            peers_other += 1
    dev.close()

    if peers_established == 0:
        print("There is no BGP peers at all!")
        exit(1)
    else:
        print("Sessions in Established state: {} out of {}".format(peers_established, peers_other + peers_established))

    if peers_other != 0:
        print("Warning: there are sessions not in Esablished state!!!!")
        exit(1)
