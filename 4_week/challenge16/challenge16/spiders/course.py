# -*- coding: utf-8 -*-
import scrapy
from challenge16.items import CourseItem


class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['github.com']
    @property
    def start_urls(self):
        url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url.format(i) for i in range(1,5))

    def parse(self, response):
        for course in response.css("li.col-12"):
            yield CourseItem({
                'name': course.css('h3 a::text').re_first("[ ]{8}(.+)"), 
                'update_time': course.css("relative-time::attr(datetime)").extract_first() 
            })
