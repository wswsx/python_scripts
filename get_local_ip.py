#!/usr/bin/env python

import socket,re,urllib2

def get_ip():
  Hostname=socket.gethostname()
  IP=socket.gethostbyname(Hostname)

  return IP


def out_ip():
  html=urllib2.urlopen('http://www.baidu.com').read()
  ip=re.search(r'\d+\.\d+\.\d+\.\d+',html).group(0)
  return ip


if __name__ == '__main__':
  local_ip=get_ip()
  to_ip=out_ip()

  print "本机IP:%s"% local_ip
  #print "外网IP:%s"% to_ip
