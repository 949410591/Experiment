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
            item = CourseItem()
            item['name'] = course.css('h3 a::text').re_first("[ ]{8}(.+)") 
            item['update_time'] = course.css("relative-time::attr(datetime)").extract_first() 

            course_url = response.urljoin(course.css("h3 a::attr(href)").extract_first())
            request = scrapy.Request(course_url, callback=self.parse_author)
            request.meta['item'] = item
            yield  request
    def parse_author(self, response):

        item = response.meta['item']
        item['commits'] = response.css("span.num.text-emphasized::text")[0].re_first("\d+")
        item['branches'] = response.css("span.num.text-emphasized::text")[1].re("\d+")
        item['releases'] =response.css("span.num.text-emphasized::text")[2].re("\d+")
        
        yield item
