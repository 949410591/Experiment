# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']
    link = LinkExtractor(restrict_xpaths = ('//li[@class="toctree-l1"]/a')) 
    rules =( 
            Rule(link,
                callback = 'parse_page',
                follow = True),
                
            )
    def parse_page(self, response):
        item = PageItem()
        item['url'] = str(response.url)
        item['text'] = response.xpath("//div[@class='body']/div").xpath("string(.)").extract_first()
        yield item
            
