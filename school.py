import urllib
import urllib2
import cookielib

filname = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filname)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
			'student':'1155125',
			'password':'892545949.jy'
	})

LoginUrl = 'http://jwxt.neuq.edu.cn/xtgl/dl_loginForward.html?_t=1496030031199'
result = opener.open(LoginUrl,postdata)
cookie.save(ignore_discard = True, ignore_discard = True)
gradeUrl = 'http://jwxt.neuq.edu.cn/cjcx/cjcx_cxDgXscj.html'
result = opener.open(gradeUrl)
print result.read()