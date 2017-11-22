import os
from scrapy import cmdline
os.chdir('Qiji_Project/spiders')
# cmdline.execute('scrapy crawl Zhilian'.split())
# 运行分布式爬虫命令
cmdline.execute('scrapy runspider Zhilian.py'.split())