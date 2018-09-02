# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import redis
import json

class FlaskDocPipeline(object):
    def process_item(self, item, spider):
        text = item["text"]
        text = re.sub("<.+?>|</.+?>","",text)
        text = re.sub(" {2,}","",b)
        item["text"] = text
        js = json.dumps(str(item))
        self.redis.lpush('flask_doc:items',js)
        return item

    def open_spider(self, spider):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)
