# #-*- coding:utf-8 -*-
# #get方法
# import urllib
# import urllib2

# values = {"username":"stuian","password":"123456"}
# data = urllib.urlencode(values)

# url = "https://passport.csdn.net/account/login"
# geturl = url + "?" + data
# request =  urllib2.Request(geturl)
# response = urllib2.urlopen(request)

# print response.read()

#-*- coding:utf-8 -*-
post方法
import urllib
import urllib2

values = {"username":"stuian","password":"123456"}
data = urllib.urlencode(values)

headers = {"userAgent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request =  urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)

print response.read()

