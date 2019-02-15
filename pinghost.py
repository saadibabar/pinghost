#!/bin/python
import subprocess
import netifaces as ni

ni.ifaddresses('eth0')
ip=ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
#print(ip)

IP2=ip.split(".")
#print (IP2[3])
    
f=open('livehosts.txt','w')

IP3=IP2[0]+'.'+IP2[1]+'.'+IP2[2]+'.'
#print(IP3)
for x in range(1,254):
    addr= IP3 + str(x)
    res=subprocess.call(['fping','-a','-q',addr],stdout=f)
