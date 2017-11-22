# -*- coding: utf-8 -*-

# Scrapy settings for Qiji_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Qiji_project'

SPIDER_MODULES = ['Qiji_project.spiders']
NEWSPIDER_MODULE = 'Qiji_project.spiders'

#url指纹过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置爬虫是否可以中断
SCHEDULER_PERSIST = True
# 设置请求队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue" # 按优先级入队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue" # 按照队列模式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack" # 按照栈进行请求的调度




# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = [
    'User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;',
    'User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
]
 # 设置随机浏览器方式
RANDOM_UA_TYPE = 'random'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Qiji_project.middlewares.QijiProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'Qiji_project.middlewares.MyCustomDownloaderMiddleware': None,
   'Qiji_project.mymiddlewares.FreeRandomProxy': 1,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'Qiji_project.pipelines.BossMysqlPipline': 1,
    'scrapy_redis.pipelines.RedisPipeline': 999,  # redis管道文件，自动把数据加载到redis
}
REDIS_HOST = '101.132.177.153'
REDIS_PORT = 61099

CONCURRENT_ITEMS = 100 # 并发解析
CONCURRENT_REQUEST = 16 # 并发请求

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
PROXIES = [
    {'host': '60.169.19.66:80'},
    {'host': '103.251.165.14:1080'},
    {'host': '185.106.121.85:1080'},
    {'host': '106.39.179.162:80'},
    {'host': '118.193.107.153:80'},
    {'host': '103.251.165.4:1080'},
    {'host': '103.251.166.14:1080'},
    {'host': '203.58.117.34:80'},
    {'host': '121.232.146.248:9000'},
    {'host': '185.106.121.196:1080'},
    {'host': '180.250.88.165:8080'},
    {'host': '116.199.2.210:82'},
    {'host': '185.82.203.85:1080'},
    {'host': '185.117.74.112:1080'},
    {'host': '185.106.121.43:1080'},
    {'host': '47.52.117.173:80'},
    {'host': '185.106.121.253:1080'},
    {'host': '50.93.197.226:1080'},
    {'host': '219.150.189.212:9999'},
    {'host': '185.106.121.194:1080'},
    {'host': '5.2.69.179:1080'},
    {'host': '123.57.76.102:80'},
    {'host': '103.251.164.7:1080'},
    {'host': '39.104.14.119:8080'},
    {'host': '172.80.118.214:1080'},
    {'host': '39.104.28.237:8080'},
    {'host': '213.163.181.33:80'},
    {'host': '36.66.38.186:8080'},
    {'host': '58.97.81.11:80'},
    {'host': '185.82.203.224:1080'},
    {'host': '202.194.14.72:8118'},
    {'host': '185.106.121.46:1080'},
    {'host': '185.117.74.125:1080'},
    {'host': '185.117.74.130:1080'},
    {'host': '185.117.74.108:1080'},
    {'host': '165.227.53.107:80'},
    {'host': '5.2.69.155:1080'},
    {'host': '118.193.107.209:80'},
    {'host': '5.2.69.184:1080'},
    {'host': '5.2.69.148:1080'},
    {'host': '5.2.69.113:1080'},
    {'host': '5.2.69.176:1080'},
    {'host': '118.70.129.102:8888'},
    {'host': '211.103.208.244:80'},
    {'host': '185.117.74.74:1080'},
    {'host': '112.114.94.161:8118'},
    {'host': '50.93.201.234:1080'},
    {'host': '5.2.69.161:1080'},
    {'host': '5.2.69.186:1080'},
    {'host': '103.251.167.8:1080'},
    {'host': '47.94.230.42:9999'},
    {'host': '39.104.14.167:8080'},
    {'host': '119.18.234.140:80'},
    {'host': '185.106.121.94:1080'},
    {'host': '119.36.92.47:80'},
    {'host': '185.117.74.100:1080'},
    {'host': '122.237.105.225:80'},
    {'host': '101.68.73.54:53281'},
    {'host': '119.36.92.41:80'},
    {'host': '185.106.121.91:1080'},
    {'host': '52.57.95.123:80'},
    {'host': '185.106.121.83:1080'},
    {'host': '113.252.236.56:8080'},
    {'host': '5.2.69.114:1080'},
    {'host': '185.106.121.90:1080'},
    {'host': '118.193.107.2:80'},
    {'host': '185.117.74.111:1080'},
    {'host': '13.73.1.69:80'},
    {'host': '5.2.69.107:1080'},
    {'host': '201.208.201.204:8080'},
    {'host': '207.165.142.35:8008'},
    {'host': '39.104.15.212:8080'},
    {'host': '35.202.143.92:80'},
    {'host': '5.2.69.190:1080'},
    {'host': '118.193.107.101:80'},
    {'host': '121.58.216.229:80'},
    {'host': '83.111.111.188:8080'},
    {'host': '103.251.166.13:1080'},
    {'host': '39.104.28.200:8080'},
    {'host': '88.99.185.134:80'},
    {'host': '120.27.10.38:8090'},
    {'host': '185.106.121.197:1080'},
    {'host': '190.73.141.202:8080'},
    {'host': '208.92.94.143:1080'},
    {'host': '124.42.7.103:80'},
    {'host': '180.183.232.126:8090'},
    {'host': '222.169.193.162:8099'},
    {'host': '116.199.2.196:80'},
    {'host': '115.79.43.156:8888'},
    {'host': '185.106.121.198:1080'},
    {'host': '201.183.227.197:8080'},
    {'host': '104.197.98.54:80'},
    {'host': '62.141.111.153:8080'},
    {'host': '103.251.167.6:1080'},
    {'host': '123.7.177.20:9999'},
    {'host': '190.107.68.62:8080'},
    {'host': '47.199.204.99:80'},
    {'host': '92.255.75.198:80'},
    {'host': '106.39.179.118:80'},
    {'host': '171.92.34.18:9000'},

]