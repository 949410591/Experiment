# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json
class DoubanMoviePipeline(object):
    def process_item(self, item, spider):

        if float(item["score"])> 8.0:   
            js = json.dumps(dict(item))
            self.redis.lpush("douban_movie:items",js)
            return item

    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

