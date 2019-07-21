#! /usr/bin/env python



from scapy.all import sniff

import decimal



def decode(pkt):

	n = decimal.Decimal(pkt.ack - 1)/1000

	o = int(n)

	c = str(unichr(int((n - int(n))*1000)))

	print "order '{0}' is '{1}'".format(o,c)



sniff(filter='tcp[tcpflags] & (tcp-syn|tcp-ack) != 0 and dst port 666', count=0, prn=decode)