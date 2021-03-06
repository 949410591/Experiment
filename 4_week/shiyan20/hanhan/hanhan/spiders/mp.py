# -*- coding: utf-8 -*-
import scrapy
from hanhan.items import MP

class MpSpider(scrapy.Spider):
    name = 'mp'
    allowed_domains = ['www.shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        for course in response.css('a.course-box'):
            item = MP()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            item['image'] = course.xpath('.//img/@src').extract_first() 

            course_url = response.urljoin(course.xpath('@href').extract_first())
            
            request = scrapy.Request(course_url, callback = self.parse_author)

            request.meta['item']  = item
            yield request

    def parse_author(self, response):
        item = response.meta['item'] 
        item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        yield item
