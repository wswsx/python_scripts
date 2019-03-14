#!/usr/bin/env python
# coding:utf8

import sys

dirfile = '/wangshixu/testxx.py'
df = open(sys.argv[1])
newdf = open(dirfile,'w')
for i in  df:
    newdf.write(i.rstrip('\n')+'\r\n')
df.close()
newdf.close()
