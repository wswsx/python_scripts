#!/usr/bin/env python
#coding:utf-8
from IPy import IP

ip_s = raw_input('请输入一个IP地址或网络地址>>>')
ips = IP(ip_s)
if len(ips) > 1: #为网络地址
    #subnet网络子网数,netaddress网络地址，netmask掩码，subnet为IP数
    print ('%-30s%-30s%-30s%-30s' %('netaddress','netmask','broadcast','subnet'))
    print ('%-30s%-30s%-30s%-30s' % (ips.net(),ips.netmask(),ips.broadcast(),len(ips)))
else: #为IP
    print ('%-30s%-30s' % ('ipaddress','iptype'))
    print ('\n%-30s%-30s' % (ips.net(),ips.iptype()))


