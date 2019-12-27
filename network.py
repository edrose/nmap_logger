#
# WIP Script to Log the availability of devices on a network
#

import sys
import os
import nmap
from time import sleep

# Define the subnet to scan here
subnet = "192.168.1.0/24"

# List the MAC addresses to track here 
tracked_mac_addrs = ["FF:FF:FF:FF:FF:FF", "FF:FF:FF:FF:FF:FF"]

# Convert all MAC addresses to uppercase
for addr in tracked_mac_addrs:
    addr = addr.upper()

# Define an array to hold  our results in. Fill with 0s
scan_results = [0] * len(tracked_mac_addrs)

# Repeat scan three times with a 10s gap between all scans
for x in range(0, 3):
    # Perform the scan
    nm = nmap.PortScanner()
    nm.scan("192.168.1.0/24", arguments='-sn')
    # Search for our target MAC addresses in the scan results 
    for h in nm.all_hosts():
        if 'mac' in nm[h]['addresses']: # MAC address doesn't always exist
            mac_addr = nm[h]['addresses']['mac']
            if mac_addr in tracked_mac_addrs:
                scan_results[tracked_mac_addrs.index(mac_addr)] |= 1
    # Sleep 10 seconds if not the last loop
    if x != 2: sleep(10)

# Just print out our results for now
print(scan_results)
        