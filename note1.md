## Python爬虫学习笔记 ##

1. Python基础知识
1. Python中urllib和urllib2库的用法
1. Python正则表达式
1. Python爬虫框架Scrapy
1. Python爬虫更高级的功能

> 1、Python基础知识 
> 
> - 廖雪峰Python教程

### 一、爬虫基础知识 ###

[http://cuiqingcai.com/942.html](http://cuiqingcai.com/942.html)

#### url的含义 ####

URL，即统一资源定位符，也就是我们说的网址，统一资源定位符是对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。

> URL的格式由三部分组成：
> 
> ①第一部分是协议(或称为服务方式)。
> 
> ②第二部分是存有该资源的主机IP地址(有时也包括端口号)。
> 
> ③第三部分是主机资源的具体地址，如目录和文件名等。

### 二、Python中urllib和urllib2库的用法 ###

#### urlopen参数 ####

    urlopen(url, data, timeout)

第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

第二三个参数是可以不传送的，data默认为空None，timeout默认为 `socket._GLOBAL_DEFAULT_TIMEOUT`

#### 构造request ####

	#-*- coding:utf-8 -*-
	import urllib2
	
	request =  urllib2.request("htttp://www.baidu.com")
	response = urllib2.urlopen(request)
	
	print response.read()

> 推荐这么写，因为显得逻辑清晰明了

> urllib2.request在python3中被改为urllib.request


此处报错了，查询官方文档urllib2.request改写为urllib2.Request

#### post和get数据传递 ####

> GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了，大家可以酌情选择。

**post方法**

	#-*- coding:utf-8 -*-
	import urllib
	import urllib2
	
	values = {"username":"stuian","password":"123456"}
	data = urllib.urlencode(values)
	
	url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
	request =  urllib2.Request(url,data)
	response = urllib2.urlopen(request)
	
	print response.read()

**get方法**

	#-*- coding:utf-8 -*-
	#get方法
	import urllib
	import urllib2
	
	values = {"username":"stuian","password":"123456"}
	data = urllib.urlencode(values)
	
	url = "https://passport.csdn.net/account/login"
	geturl = url + "?" + data
	request =  urllib2.Request(geturl)
	response = urllib2.urlopen(request)
	
	print response.read()

#### Urllib库的高级用法 ####

**设置Headers**

1、agent就是请求的身份，如果没有写入请求身份，那么服务器不一定会响应，所以可以在headers中设置agent

2、对付”反盗链”的方式，对付防盗链，服务器会识别headers中的referer是不是它自己，如果不是，有的服务器不会响应，所以我们还可以在headers中加入referer

	#-*- coding:utf-8 -*-
	post方法
	import urllib
	import urllib2
	
	values = {"username":"stuian","password":"123456"}
	data = urllib.urlencode(values)
	
	headers = {"userAgent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"，
	referer:
              }
	
	url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
	request =  urllib2.Request(url,data,headers)
	response = urllib2.urlopen(request)
	
	print response.read()

**headers其他属性**

> User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
> 
> Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
> 
> application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
> 
> application/json ： 在 JSON RPC 调用时使用
> 
> application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
> 
> 在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务

#### Proxy（代理）的设置 ####

> urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了

#### 使用 HTTP 的 PUT 和 DELETE 方法 ####

> 如果要使用 HTTP PUT 和 DELETE ，只能使用比较低层的 httplib 库。

    import urllib2
    request = urllib2.Request(url, data = data)
    request.get_method = lambada: 'PUT' # or 'DELETE'
    reponse = urllib2.urlopen(request)

#### 使用debuglog ####

打开debug log的方法：

    import urllib2
    httpHandler = urllib2.HTTPHandler(debuglevel=1)
    httpsHandler = urllib2.HTTPSHander(debuglevel=1)
    opener = urllib2.build_opener(httpHandler, httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')

### URLError错误处理 ###

#### urlerror ####

用try-except语句来检验是否出错

import urllib2

request = urllib2.Request('http://www.xxx.com')

try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.reason

#### HTTPError ####

- 100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
- 101： 转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
- 102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
- 200：请求成功      处理方式：获得响应的内容，进行处理
- 201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到
- 202：请求被接受，但处理尚未完成    处理方式：阻塞等待
- 204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
- 300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
- 301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
- 302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL
- 304：请求的资源未更新     处理方式：丢弃
- 400：非法请求     处理方式：丢弃
- 401：未授权     处理方式：丢弃
- 403：禁止     处理方式：丢弃
- 404：没有找到     处理方式：丢弃
- 500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
- 501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
- 502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
- 503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。

> 我们知道，HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常，所以上述的代码可以这么改写

	import urllib2
	 
	req = urllib2.Request('http://blog.csdn.net/cqcre')
	try:
	    urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.code
	except urllib2.URLError, e:
	    print e.reason
	else:
	    print "OK"

如果捕获到了HTTPError，则输出code，不会再处理URLError异常。如果发生的不是HTTPError，则会去捕获URLError异常，输出错误原因。

另外还可以加入 hasattr属性提前对属性进行判断，代码改写如下:

	import urllib2
	
	req = urllib2.Request('http://blog.csdn.net/cqcre')
	try:
		urllib2.urlopen(req)
	except urllib2.URLError, e:
		if hasattr(e,"reason"):
			print e.reason
	else:
		print "ok"

### Cookie的使用 ###

Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）

比如说有些网站需要登录后才能访问某个页面，在登录之前，你想抓取某个页面内容是不允许的。那么我们可以利用Urllib2库保存我们登录的Cookie，然后再抓取其他页面就达到目的了。

#### opener ####

当你获取一个URL你使用一个opener(一个urllib2.OpenerDirector的实例)。在前面，我们都是使用的默认的opener，也就是urlopen。它是一个特殊的opener，可以理解成opener的一个特殊实例，传入的参数仅仅是url，data，timeout。

如果我们需要用到Cookie，只用这个opener是不能达到目的的，所以我们需要创建更一般的opener来实现对Cookie的设置。

#### cookielib ####

cookielib模块的主要作用是提供可存储cookie的对象，该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。

它们的关系：CookieJar —-派生—->FileCookieJar  —-派生—–>MozillaCookieJar和LWPCookieJar

**获取cookie保存到变量**
	
	import urllib2
	import cookielib
	#声明一个cookiejar对象实例来保存cookie
	cookie = cookielib.CookieJar()
	#利用urllib2库的httpcookieprocessor对象来创建cookie处理器
	handler = urllib2.HTTPCookieProcessor(cookie) 
	#通过handler来构建opener
	opener = urllib2.build_opener(handler)
	#此处的open方法同urllib2的urlopen方法，也可以传入request
	response = opener.open('http://www,baidu.com')
	for item in cookie:
		print 'Name = ' + item.name
		print 'Value = ' + item.value
	
#### 保存cookie到文件 ####

import cookielib
import urllib2

	#设置保存cookie的文件，同级目录下的cookie.txt
	filename = 'cookie.txt'
	#声明一个MozillaCookieJar对实例来保存cookie，之后写入文件
	cookie = cookielib.MozillaCookieJar(filename)
	#利用urllib2库的httpcookieprocessor对象来创建cookie处理器
	handler = urllib2.HTTPCookieProcessor(cookie) 
	#通过handler来构建opener
	opener = urllib2.build_opener(handler)
	#此处的open方法同urllib2的urlopen方法，也可以传入request
	response = opener.open('http://www,baidu.com')
	#保存cookie到文件
	cookie.save(ignore_discard = True, ignore_expires = Ture)

> ignore_discard的意思是即使cookies将被丢弃也将它保存下来，ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入

**从文件中获取cookie并访问**

	import cookielib
	import urllib2
	
	#创建MozillaCookieJar实例对象
	cookie = cookielib.MozillaCookieJar()
	#从文件中读取cookie内容到变量
	cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)
	#创建请求的request
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
	response = opener.read(req)
	print response.read()

**利用cookie模拟网站登录**

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

### 正则表达式 ###

