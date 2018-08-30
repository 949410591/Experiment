# -*- coding: utf-8 -*-
import scrapy
from hanhan.items import CoursesImageItem

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['www.shiyanlou.com']
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        item = CoursesImageItem()
        item['image_urls'] = response.xpath('//div[@class="course-img"]/img/@src').extract()
        yield item


