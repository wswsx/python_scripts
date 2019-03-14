#!/usr/bin/env python
#coding:utf-8

import time
import psutil
import datetime
now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
print ('*' * 107)
print ('%-30s%-30s' %('当前系统时间','系统启动时间'))
print ('%-24s%-24s' %(now_time,boot_time))
print ('*' * 107)


#系统用户
users_count = len(psutil.users())
users_list = ",".join([u.name for u in psutil.users()])
print(u"当前有%s个用户连接系统，分别是 %s" % (users_count, users_list))


#物理cpu个数
print ("物理cpu个数为: %s " % psutil.cpu_count(logical=False))

#cpu使用率
cpu = (str(psutil.cpu_percent(1))) + '%'
print ('cpu使用率：%s' % cpu )

#内存信息
Free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 ), 2))
Total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 ), 2))
Used = str(round(psutil.virtual_memory().used / (1024.0 * 1024.0 ), 2))
Memory = float(Used)/float(Total)
Buffers = str(round(psutil.virtual_memory().buffers / (1024.0 * 1024.0 ), 2))
Cached = str(round(psutil.virtual_memory().cached / (1024.0 * 1024.0 ), 2))
print('*'* 49 +'内存信息' + '*' * 49  )
total = 'total(M)'
free = 'free(M)'
used = 'used(M)'
buffers = 'buffers(M)'
cached = 'cached(M)'
percent = 'percent(%)'
print ('%-15s%-15s%-15s%-15s%-15s%-15s' % (total,free,used,percent,buffers,cached))
print ('%-15s%-15s%-15s%-15s%-15s%-15s' %(Total,Free,Used,round(Memory*100,2),Buffers,Cached))
   
print('*'* 49 +'磁盘信息' + '*' * 49  )
dev = psutil.disk_partitions()
name = 'name'
mount = 'mount'
total = 'total(G)'
free = 'free(G)'
used = 'used(G)'
print ("%-25s%-35s%-25s%-15s%-10s" %(name,mount,total,free,used))
for d in dev:
   io =  psutil.disk_usage(d.mountpoint)
   print ("%-25s%-35s%-25s%-15s%-10s" %(d.device,d.mountpoint,round(io.total/(1024.0*1024.0*1024.0),2),round(io.free/(1024.0*1024.0*1024.0),2),round(io.used/(1024.0*1024*1024.0),2)))
