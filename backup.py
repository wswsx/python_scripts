#!/usr/bin/env python
#coding:utf-8
#这是一个完全备份和增量备份的脚本

import os
import hashlib
import tarfile
import cPickle as p
import time

base = '/etc'
src  = 'yum.repos.d'
dst  = 'yum.repos.d.bak'
md5file = os.path.join(base,dst,'md5.data')
fullname = 'full_src%s.tar.gz' % (time.strftime('%Y%m%d'))
incname  = 'inc_src%s.tar.gz' % (time.strftime('%Y%m%d'))

def fullbackup():#完全备份
    os.chdir(base)
    tar = tarfile.open(os.path.join(base,dst,fullname),'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}
    for eachline in os.listdir(os.path.join(base,src)):
        fullpath = os.path.join(base,src,eachline)
        md5dict[eachline] = md5sum(fullpath)

    with open(md5file,'w') as f:
        p.dump(md5dict,f)


def incbackup():#增量备份
    os.chdir(base)
    with open(md5file) as f:
        storedmd5 = p.load(f)

    newmd5 = {}
    for eachline in os.listdir(os.path.join(base,src)):
        fullpath = os.path.join(base,src,eachline)
        newmd5[eachline] = md5sum(fullpath)

    tar = tarfile.open(os.path.join(base,dst,incname),'w:gz')
    for eachkey in newmd5:
        if (eachkey not in storedmd5) or (newmd5[eachkey] != storedmd5[eachkey]):
            tar.add(os.path.join(src,eachkey))
            tar.close()

    with open(md5file,'w') as f:
        p.dump(newmd5,f)

def md5sum(fname):#获取文件md5码值
    m = hashlib.md5()
    with open(fname) as f:
        while True:
            data = f.read(4096)
            if len(data) == 0:
                break
            m.update(data)
    return m.hexdigest()


def main():
     if time.strftime('%a') == 'Mon':
         fullbackup()
     else:
         incbackup()

if  __name__ == '__main__':
    main()

        
