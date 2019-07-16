#!/usr/bin/python

import sys
import requests
import json
import traceback
import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## https://teslapw/api/meters/aggregates

sw_url = sys.argv[1]
services = sys.argv[2:]

print sw_url
#print services


try:
    req=requests.get(sw_url, verify=False)
    #print req.status_code
    #print (req.json())
    data = req.json()
    print(data['battery']) # PW
    print(data['solar'])   # Solar
    print(data['load'])    # Home
    print(data['site'])    # Grid 
   
    #req.json().json.dumps(parsed, indent=4, sort_keys=True)
except:
    print 'An error occurred:'
    traceback.print_exc()
    #print '2 dynserv_' + dynsvc + ' - CRITICAL - service wizard reports service ' + dynsvc + ' does not exist'
    
    
svcstate=0
svcstatetext='OK'
svcstate='OK'
if svcstate == 'OK':
    svcstate=0
    svcstatetext='OK'
else:
    svcstate=2
    svcstatetext='CRITICAL'

### See https://checkmk.com/cms_localchecks.html for local check documentation

#print str(svcstate) + ' dynserv_' + dynsvc + ' - ' + svcstatetext + ' - service ' + dynsvc + ' reports state ' + dynsvcstate
