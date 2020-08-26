import scrapy


class Maoyantop10Spider(scrapy.Spider):
    name = 'maoyantop10'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
