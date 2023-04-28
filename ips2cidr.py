import ipaddress
from collections import defaultdict
from tabulate import tabulate
import pandas as pd

user_input = input("Enter List of CIDRs Comma Separated: ")
given_ranges = [ipaddress.ip_network(range) for range in user_input.split(',')]

ip_list_count = 0
unaccounted = set()
accounted = defaultdict(list)

# Requires a file of discovered hosts titled ip_list.txt
with open('ip_list.txt', 'r') as f:
    for line in f:
        ip = line.strip()
        ip_list_count += 1
        for range in given_ranges:
            if ipaddress.ip_address(ip) in range:
                accounted[str(range)].append(ip)
                break
        else:
            unaccounted.add(ip)

print('===================================')
print('| CIDR Range\t| Uphost Count      |')
print('===================================')


new_unaccounted = 0
for k, v in accounted.items():
    new_unaccounted += len(v)
    print('| {}\t|\t{}\t   |'.format(k, len(v)))
    print('-----------------------------------')

print('IPs Unaccounted for: {}'.format(ip_list_count - new_unaccounted))
