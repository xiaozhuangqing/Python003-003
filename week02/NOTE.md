学习笔记

本周学西了一下内容
	1 python的异常与捕获，这块内容跟其他语言大差不差，try except finnly,
	有一个python的特色，with，代替try except 的使用，主要用在上下文管理，比		如打开文件操作，with open 很方便
	2 python连接数据库，包括MySQL 与redis ，分队对应pymysql,server-redis包，	操作的讨论基本三步走，连接，执行，断开连接
	3 爬虫的增强功能： 模拟浏览器的头部，模拟登入获得cookie，webdriver模拟浏	览器，图片验证码的识别，使用代理IP

问题：
	在学习自定义中间件，随机代理IP中，本机爬虫运行时一直报错,具体如下：
	2020-08-30 17:53:03 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
	2020-08-30 17:53:05 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://httpbin.org/robots.txt> (failed 1 times): Connection was refused by other side: 10061: 由于目标计算机积极拒绝，无法连接。.
	2020-08-30 17:53:07 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://httpbin.org/robots.txt> (failed 2 times): [<twisted.python.failure.Failure twisted.internet.error.ConnectionDone: Connection was closed cleanly.>]
	2020-08-30 17:53:10 [scrapy.downloadermiddlewares.retry] ERROR: Gave up retrying <GET http://httpbin.org/robots.txt> (failed 3 times): Connection was refused
	by other side: 10061: 由于目标计算机积极拒绝，无法连接。.
	2020-08-30 17:53:10 [scrapy.downloadermiddlewares.robotstxt] ERROR: Error downloading <GET http://httpbin.org/robots.txt>: Connection was refused by other side: 10061: 由于目标计算机积极拒绝，无法连接。.
	Traceback (most recent call last):
	  File "c:\users\xiao\appdata\local\programs\python\python37\lib\site-packages\scrapy\core\downloader\middleware.py", line 44, in process_request
	      return (yield download_func(request=request, spider=spider))
	      twisted.internet.error.ConnectionRefusedError: Connection was refused by other side: 10061: 由于目标计算机积极拒绝，无法连接。.
	      2020-08-30 17:53:11 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://httpbin.org/ip> (failed 1 times): 500 Internal Server Error
	      2020-08-30 17:53:12 [scrapy.downloadermiddlewares.retry] DEBUG: Retrying <GET http://httpbin.org/ip> (failed 2 times): 500 Internal Server Error
	      2020-08-30 17:53:14 [scrapy.downloadermiddlewares.retry] ERROR: Gave up retrying <GET http://httpbin.org/ip> (failed 3 times): 500 Internal Server Error
	      2020-08-30 17:53:14 [scrapy.core.engine] DEBUG: Crawled (500) <GET http://httpbin.org/ip> (referer: None)
	      2020-08-30 17:53:15 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <500 http://httpbin.org/ip>: HTTP status code is not handled or not allowed
	      2020-08-30 17:53:15 [scrapy.core.engine] INFO: Closing spider (finished)
	      2020-08-30 17:53:15 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
	      {'downloader/exception_count': 3,
	       'downloader/exception_type_count/twisted.internet.error.ConnectionRefusedError': 2,
	        'downloader/exception_type_count/twisted.web._newclient.ResponseNeverReceived': 1,
	
	针对上述问题，目前还没有找到合适的方法解决，希望以后可以解决。
