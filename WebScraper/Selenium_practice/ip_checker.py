# coding=utf-8

import urllib
import socket

socket.setdefaulttimeout(3)

# 这里打开刚才存ip的文件
ip_info = open("ip.txt")    
lines = ip_info.readlines()
proxys = []
for i in range(0,len(lines)):
    proxy_host = "http://" + lines[i]
    proxy_temp = {"http":proxy_host}
    proxys.append(proxy_temp)

# 用网页去验证，遇到不可用IP抛异常
url = "http://ip.chinaz.com/getip.aspx"
# 将可用IP写入valid_ip.txt
output_file = open("valid_ip.txt", "a+")

for proxy in proxys:
    try:
        res = urllib.urlopen(url,proxies=proxy).read()
        valid_ip = proxy['http'][7:]
        print 'valid_ip: ' + valid_ip
        output_file.write(valid_ip)
        output_file.flush()
    except Exception,e:
        print proxy
        print e
        continue