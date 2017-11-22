# -*- coding: utf-8 -*-
import scrapy,re,datetime

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#分布式爬虫
from scrapy_redis.spiders import RedisCrawlSpider


class ZhilianSpider(RedisCrawlSpider):
    name = 'Zhilian'
    allowed_domains = ['zhaopin.com']
    # 利用redis启动爬虫的钥匙
    redis_key = 'Zhilian:start_urls'
    # start_urls = ['http://sou.zhaopin.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'sou.zhaopin.com'), follow=False),
        # Rule(LinkExtractor(allow='/jobs/searchresult\.ashx'), follow=True),
        # Rule(LinkExtractor(allow=r'xiaoyuan.zhaopin.com'),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'\d+.htm', deny=(r'company')), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow='/jobs/searchresult\.ashx\?jl=\d+&bj=\d+&sj=\d+',deny=r're=\d+'), follow=True),

    )

    num_pattern = re.compile(r'\d+')
    def parse_item(self, response):
        item = {}
        url = response.url
        pname = response.xpath('//div[@class="top-fixed-box"]/div[1]//h1/text()').extract()
        if pname:
            pname = pname[0]
        else:
            pname = None
        company = response.xpath('//div[@class="top-fixed-box"]/div[1]//h2/a/text()').extract()
        if company:
            company = company[0]
        else:
            company = None
        advantage = response.xpath('//div[@class="welfare-tab-box"][1]//span/text()').extract()
        if advantage:
            advantage = ','.join(advantage)
        else:
            advantage = None
        date_pub = response.xpath('//div[@class="terminalpage-left"]/ul/li[3]/strong/span/text()').extract()
        if date_pub:
            date_pub = ''.join(date_pub).split(' ')[0]
        else:
            date_pub = None
        money = response.xpath('//div[@class="terminalpage-left"]/ul/li[1]/strong/text()').extract()
        try:
            if '面议' not in money:
                money = money[0]
                res = self.num_pattern.findall(money)
                smoney = res[0]
                emoney = res[1]
            else:
                smoney = '面议'
                emoney = '面议'
        except:
            smoney = None
            emoney = None
        location = response.xpath('//div[@class="terminalpage-left"]/ul/li[2]/strong/a/text()').extract()
        if location:
            location = location[0]
        else:
            location = None
        year = response.xpath('//div[@class="terminalpage-left"]/ul/li[5]/strong/text()').extract()
        try:
            if '不限' not in year:
                year = year[0]
                res = self.num_pattern.findall(year)
                syear = res[0]
                eyear = res[1]
            else:
                syear = '不限'
                eyear = '不限'
        except:
            syear = None
            eyear = None
        degree = response.xpath('//div[@class="terminalpage-left"]/ul/li[6]/strong/text()').extract()
        if degree:
            degree = degree[0]
        else:
            degree = None
        num = response.xpath('//div[@class="terminalpage-left"]/ul/li[7]/strong/text()').extract()
        if num:
            num = num[0]
            if '人' in num:
                num = num.strip('人')
        else:
            num = None
        ptype = response.xpath('//div[@class="terminalpage-left"]/ul/li[8]/strong/a/text()').extract()
        if ptype:
            ptype = ptype[0]
        else:
            ptype = None
        jobdesc = response.xpath('//div[@class="tab-inner-cont"][1]/p/text()').extract()
        if jobdesc:
            jobdesc = ''.join(jobdesc).strip()
        else:
            jobdesc = None
        jobaddr = response.xpath('//div[@class="tab-inner-cont"]//h2/text()').extract()
        if jobaddr:
            jobaddr = jobaddr[0].strip()
        else:
            jobaddr = None
        crawl_time = datetime.datetime.now().strftime('%Y-%m-%d')

        item['url'] = url
        item['pname'] = pname
        item['smoney'] = smoney
        item['emoney'] = emoney
        item['location'] = location
        item['syear'] = syear
        item['eyear'] = eyear
        item['degree'] = degree
        item['ptype'] = ptype
        # item['tags'] = ''
        item['date_pub'] = date_pub
        item['advantage'] = advantage
        item['jobdesc'] = jobdesc
        item['jobaddr'] = jobaddr
        item['company'] = company
        item['crawl_time'] = crawl_time
        item['num'] = num
        yield item



        # print(url,pname,company,advantage,date_pub,smoney,emoney,location,syear,eyear,degree,num,ptype,jobdesc,jobaddr,crawl_time)
    #处理元/月 的函数
    def process_money(self,value):
        pass
