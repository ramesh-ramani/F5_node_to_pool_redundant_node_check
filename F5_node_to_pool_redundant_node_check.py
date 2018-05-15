from f5.bigip import ManagementRoot
import certifi
import urllib3
import requests
import re
from  __builtin__ import any


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
x_file = open('/usr/local/bin/python_scripts/nodes.txt', 'r')
r=list()
s=list()
for i in x_file:
    i=i.split('\n',1)[0]
    r.append(i)
#print r
# Connect to the BigIP
mgmt = ManagementRoot("10.50.0.240", "user", "pwd")
x_file=open('nodes.txt', 'r')

# Get a list of all pools on the BigIP and print their names and their
# members' names
#test=list()
pools = mgmt.tm.ltm.pools.get_collection()

##Below lines will print pool and pool members##

dict={}

#for pool in pools:
#     s=pool.name
#     print "Pool is:{} ".format(s)
#     for member in pool.members_s.get_collection():
#         t=member.name
#         print "members are: {}".format(t)

for pool in pools:
    test=list()
    t=list()
    u=list()
    for member in pool.members_s.get_collection():
          test.append((member.name).encode("utf-8"))
    for line in r:
        for i in test:
            if line in i:
               s.append((pool.name).encode("utf-8"))
               break
            else: continue
#print s
#sample=list()
for pool in pools:
    sample=list()
    man=list()
    for i in s:
        if pool.name not in i: continue
        else: 
            print pool.name
            for member in pool.members_s.get_collection():
                sample.append((member.name).encode("utf-8"))
                print member.name
                words = ["001","002"]
            if all('002' and '001' in i for i in sample): print "!!!NO REDUNDANT MEMBERS AVAILABLE!!!"'\n'
            else: print "***REDUNDANT MEMBERS AVAILABLE***"'\n'
