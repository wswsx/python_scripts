#!/usr/bin/python
#-*- coding: utf-8 -*-
from ftplib import FTP

class MyData(object):
	
	  def __init__(self):
	      self.ftp = ftplib.FTP()

    def ftpconnect(self,host, username, password):
        #ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
        self.ftp.connect(host, 21)          #连接
        self.ftp.login(username, password)  #登录，如果匿名登录则用空串代替即可
        
        
    def downloadfile(self, remotepath, localpath):
        bufsize = 1024                #设置缓冲块大小
        fp = open(localpath,'wb')     #以写模式在本地打开文件
        self.ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
        self.ftp.set_debuglevel(0)         #关闭调试
        fp.close()                    #关闭文件
    
    def uploadfile(self, remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'rb')   #以读模式打开本地文件
        self.ftp.storbinary('STOR '+ remotepath , fp, bufsize) #上传文件
        self.ftp.set_debuglevel(0)
        fp.close()                                    
    

    
def main():
    myftp = MyData()
    myftp.ftpconnect('localhost','ftp','')
    myftp. downloadfile('/pub/CentOS-Debuginfo.repo','test.txt')

if __name__ == '__main__':
	  main()