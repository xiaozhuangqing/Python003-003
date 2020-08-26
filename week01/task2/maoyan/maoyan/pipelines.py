# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanPipeline:
    def process_item(self, item, spider):
        movie_name = item['movie_name']
	movie_types = item['movie_types']
	movie_release = item['movie_release']

	output = f'|{movie_name}|\t|{movie_types}|\t|{movie_release}|\n\n'
	with open('./doubanmovie.txt','a+',encoding='utf-8') as article:
	    article.write(output)
	
	return item
