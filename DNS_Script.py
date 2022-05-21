#!/usr/bin/env python3

# Import libraries
from datetime import datetime
from pprint import pprint

import dns.resolver
import pygsheets

gc = pygsheets.authorize(client_secret='client_secret.json')

sh = gc.open_by_key('1fed131btfM_rLMATQrgyPZHsavXoH23mRbQjkqNed6Q')

wk1 = sh.sheet1

column_1 = wk1.get_col(1,include_tailing_empty=False)[1:]

next_col = len(wk1.get_row(1, include_tailing_empty=False)) + 1 

resolver = dns.resolver.Resolver(configure=False)
resolver.timeout = 1 
resolver.nameservers = [
    "8.8.8.8",  # google
    "1.1.1.1",  # cloudflare
    "205.171.3.66",  # lumen
    "199.85.127.30",  # ultradns
]

# Empty list for output 
a_record_results = [datetime.today().strftime("%Y-%m-%d")]  # 2022-05-11

for val in column_1:
    val = val.split("/")[0].strip()
    try:
        output = dns.resolver.query(val, "A")
        """object to to_text
        put them in sort() to order them
        join together as a single string"""



        #a_record_results.append(output[0].to_text())
        # for ip in output:     
        #    a_record_results.append(ip.to_text())

    except dns.exception.DNSException as err:
        print(err)
        a_record_results.append('No A Record')

    else:
        ip_strings = []
        for ips in output:
            ip_string = ips.to_text()
            ip_strings.append(ip_string)
        
        ip_strings.sort()

        url_string = ", ".join(ip_strings)
        a_record_results.append(url_string)

pprint(a_record_results)
print(len(column_1))
print(len(a_record_results))

wk1.update_col(next_col, a_record_results)    







