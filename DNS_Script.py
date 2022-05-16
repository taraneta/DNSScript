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


urls = [
'www.israel.tv',
'www.israeli.tv',
'www.israeltv.com',
'www.israel-tv.xyz',
'www.zira.to',
'www.t2m.is.isr',
'www.t2m.ac/zira',
'www.cutt.ly/6DDhRau',
'www.t2m.ac/cht',
'www.israeltv.to',
'www.isr.dev',
'www.israeli-tv.com',
'www.sdarot.tv',
'www.sdarot.world',
'www.sdarot.work',
'www.sdarot.pro',
'www.sdarot.dev',
'www.sdarot.casa',
'www.hasdarot.cc',
'www.lametrofitness.net',
'www.hasdarot.life',
'www.sdarot.buzz',
'www.hasdarot.live',
'www.hasdarot.space',
'www.hasdarot.pro',
'www.hasdarot.club/NameCheap',
'www.sdarot.today',
'www.sdarot.rocks',
'www.hasdarot.xyz',
'www.sdarot.pm',
'www.hasdarot.net',
'www.hasdarot.tv',
'www.sforum.tv',
'www.sdarot.space',
'www.taxisinyork.co.uk',
'www.gamersbay.online',
'www.farmakeio.online',
'www.oneeing.info',
'www.seedingchange.co.uk/index',
'www.gwp-conductive.co.uk/index',
'www.sdarot.life',
'www.sdarot.services',
'www.sdarot.space',
'www.sdarot.website',
'www.sdarot.work',
'www.sdarot.video',
'www.hasdarot.co',
'www.sirtonim.tv',
'www.sdarot.me',
'www.flarehost.org',
'www.hostonline.site',
'www.mosalsalat.tv',
'www.zira.ninja',
'www.zira.online',
'www.sdarot.biz',
'www.tmbt.club',
'www.theploggers.com',
'www.speedybusinessnetworking.com',
'www.shellindir.info',
'www.zpqbae.com',
'www.stt3888.com',
'www.oneeing.info',
'www.sdarot.ninja',
'www.sdarot.live',
'www.sdarot.click',
'www.prezenti.site',
'www.ortegasport.com',
'www.lookmovies.watch',
'www.gldbr.com',
'www.dot26.xyz',
'www.dev0oo0o00000oo00oo.xyz',
'www.cdnsec.com',
]


resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = [
    "8.8.8.8",  # google
    "1.1.1.1",  # cloudflare
    "205.171.3.66",  # lumen
    "199.85.127.30",  # ultradns
]


# Printing record
a_record_results = []

for val in column_1:
    try:
        #print(val)
        output = resolver.query(val, "A")
        a_record_results.append(a_record_results)
        # print(val + output)
        
    except: 
        dns.exception.DNSException()
        #output.update_col('2',output)
        a_record_results.append("err")
    
wk1.update_col(2, a_record_results)

