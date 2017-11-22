# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import datetime
from scrapy_redis.spiders import RedisCrawlSpider

class BossSpider(RedisCrawlSpider):
    name = 'Boss'
    # allowed_domains = ['http://www.zhipin.com/']
    # start_urls = ['http://www.zhipin.com/']
    redis_key = 'Boss:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'zhipin.com/[a-z]\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/job_detail/\d+.html'), callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=r'zhipin.com/[a-z]\d+'), follow=True),

    )

    def parse_item(self, response):
        item = {}
        url = response.url
        pname = response.xpath('//div[@class="info-primary"]//div[@class="name"]/text()').extract()[0]
        money = response.xpath('//div[@class="info-primary"]//div[@class="name"]/span/text()').extract()[0]
        smoney = money.split('-')[0].strip('K')
        emoney = money.split('-')[1].strip('K')
        location = response.xpath('//div[@class="info-primary"]//p/text()').extract()[0]
        year = response.xpath('//div[@class="info-primary"]//p/text()').extract()[1]
        if '-' in year:
            syear = year.split('-')[0]
            eyear = year.split('-')[1].strip('年')
        else:
            syear = year[0]
            eyear = year[0]
        degree = response.xpath('//div[@class="info-primary"]//p/text()').extract()[2]
        ptype = response.xpath('//div[@class="info-company"]/p/a/text()').extract()[0]
        tags = response.xpath('//div[@class="info-primary"]//div[@class="job-tags"]/span/text()').extract()[0]
        date_pub = response.xpath('//div[@class="info-primary"]//div[@class="job-author"]/span/text()').extract()[0]
        advantage = None
        jobdesc  = response.xpath('//div[@class="detail-content"]//div[@class="text"]/text()').extract()[0].strip()
        jobaddr = response.xpath('//div[@class="detail-content"]//div[@class="location-address"]/text()').extract()[0].strip()
        company = response.xpath('//div[@class="info-company"]/h3/a/text()').extract()[0]
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')
        num = None
        print(pname,smoney,emoney,location,syear,eyear,degree,ptype,tags,date_pub,advantage,jobdesc,jobaddr,company,crawl_time,num)




        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['ptype'] = ptype
        item['tags'] = tags
        item['date_pub'] = date_pub
        item['advantage'] = advantage
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['crawl_time'] = crawl_time
        item['num'] = num
        yield item
