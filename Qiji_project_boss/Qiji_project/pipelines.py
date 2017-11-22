# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class QijiProjectPipeline(object):
    def process_item(self, item, spider):
        return item
#数据库公共类
class MysqlPipline(object):
    def __init__(self):
        self.conn = pymysql.connect('rm-uf6gz5q242iynpgzao.mysql.rds.aliyuncs.com','root','QJ*python03^job','qiji_project',charset='utf8')
        self.cursor = self.conn.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
#存入数据库
class BossMysqlPipline(MysqlPipline):
    def process_item(self,item,spider):
        if spider.name == 'Boss':
            sql = 'insert into boss_job(url,pname,smoney,emoney,location,syear,eyear,degree,ptype,tags,date_pub,advantage,jobdesc,jobaddr,company,crawl_time,num) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update pname=values(pname),smoney=values(smoney),num=values(num ) '
            parms = (item['url'],item['pname'],item['smoney'],item['emoney'],item['location'],item['syear'],item['eyear'],item['degree'],item['ptype'],item['tags'],item['date_pub'],item['advantage'],item['jobdesc'],item['jobaddr'],item['company'],item['crawl_time'],item['num'])

            try:
                self.cursor.execute(sql,parms)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
                print('执行sql语句失败')
        return item


