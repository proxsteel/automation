#!/usr/bin/env python3

my_interfaces = ['ge-0/0/0', 'ge-0/0/1', 'xe-1/0/0', 'xe-1/0/1', 'gr-0/0/0']

for interf in my_interfaces:
    if interf.startswith('ge-'):
        print("{} is a 1G interface".format(interf))
    elif interf.startswith('xe-'):
        print("{} is a 10G interface".format(interf))
    else:
        print("\nThe interface type of {} couldn\'t be recognized\n\n".format(interf))

print("Test finished!!!")
