#!/usr/bin/env python3

# Import libraries
from datetime import datetime
from pprint import pprint

import dns.resolver
import pygsheets

gc = pygsheets.authorize(client_secret='client_secret.json')

sh = gc.open_by_key('1fed131btfM_rLMATQrgyPZHsavXoH23mRbQjkqNed6Q')

wk1 = sh.sheet1

column_1 = wk1.get_col(1, include_tailing_empty=False)

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = [
    "8.8.8.8",  # google
    "1.1.1.1",  # cloudflare
    "205.171.3.66",  # lumen
    "199.85.127.30",  # ultradns
]

# Empty list for output 
a_record_results = []

for val in column_1:
    try:
        output = resolver.query(val, "A")
        a_record_results.append(output)
        
    except: 
        dns.exception.DNSException()
        a_record_results.append('err')
    

wk1.update_col(2, a_record_results)

