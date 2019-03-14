#!/usr/bin/env python
#coding:utf-8
import os,sys
ls = os.linesep
while True:
    filename = raw_input("请输入一个文件名： ")
    if os.path.exists(filename):
        print "Error: '%s 已经存在请重新输入'" % filename
    else:
        break
all=[]
print "\n请输入内容以.结束："
while True:
    charlist = raw_input(">")
    if charlist == '.':
        break
    all.append(charlist)
bos = open(filename,'w')
bos.writelines(['%s%s'% (x,ls) for x in all ])
bos.close()

print "Done"

