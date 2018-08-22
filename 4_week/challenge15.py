import scrapy

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        url = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url.format(i) for i in range(1,5))

    def parse(self,response):
        for course in response.css('li.col-12'):
            yield{
                    'name': course.css('h3 a::text').re_first("[ ]{8}(.+)"), 
                    'datetime': course.css("relative-time::attr(datetime)").extract_first() 
                }
