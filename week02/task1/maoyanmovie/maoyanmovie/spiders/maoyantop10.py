import scrapy
from maoyanmovie.items import MaoyanItem
from scrapy.selector import Selector

class Maoyantop10Spider(scrapy.Spider):
    name = 'maoyantop10'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = f'https://maoyan.com/films'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self,response):
        tags = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')[:10]
        for tag in tags:
            url = f'https://maoyan.com' + tag.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url,callback=self.parse2)


    def parse2(self,response):
        Selector(response=response).xpath
        item = MaoyanItem()

        # 电影名称
        movie_name = Selector(response=response).xpath('//h1[@class="name"]/text()').extract_first()

        # 电影类型
        all_list = Selector(response=response).xpath('//li[@class="ellipsis"][1]')
        movie_type_tags = all_list.xpath('./a[@class="text-link"]')
        movie_types = ''
        for movie_type_tag in movie_type_tags:
            movie_type = movie_type_tag.xpath('text()').extract_first().strip()
            movie_types = movie_types + movie_type + '/'
        movie_types = movie_types[:-1]

        #电影上映日期
        movie_release = Selector(response=response).xpath('//li[@class="ellipsis"][3]/text()').extract_first()[:10]

        #写入item

        item['movie_name'] = movie_name
        item['movie_types'] = movie_types
        item['movie_release'] = movie_release
        yield item