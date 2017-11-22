from scrapy import cmdline
import os
os.chdir('Qiji_Project/spiders')
# cmdline.execute('scrapy crawl Boss'.split())
cmdline.execute('scrapy runspider Boss.py'.split())