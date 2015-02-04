#-*-coding:utf-8-*-
import urllib2,time
t1 = time.time()
for i in range(99):
    t = i+1
    url = "http://210.242.125.%d"%t
    req = urllib2.Request(url)
    try:
        google = urllib2.urlopen(req,data = None,timeout=1)
        cheak = int(google.getcode())
        if cheak == 200:
            o = file('url.txt','a')
            o.write(url)
            o.write("\n")
            o.flush()
            o.close()
            print '<%s> 可以使用!'%url
    except(IOError):
        #print "[%s] is not work"%url
        pass
t2 = time.time()
t = str(t2-t1)
print '共用时%s秒'%t
