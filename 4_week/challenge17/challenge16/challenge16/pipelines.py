# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from challenge16.models import Repository, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime 

class Challenge16Pipeline(object):
    def process_item(self, item, spider):
        item["update_time"] = datetime.strptime(item['update_time'],'%Y-%m-%dT%H:%M:%SZ').strftime("%Y-%m-%d %H:%M:%S")
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        self.session = sessionmaker(bind=engine)()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

