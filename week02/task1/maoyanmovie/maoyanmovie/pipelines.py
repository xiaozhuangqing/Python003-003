# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:

    def __init__(self):
        # 建立连接
        # self.conn = pymysql.connect('localhost','root','root','test')  # 有中文要存入数据库的话要加charset='utf8'

        self.conn = pymysql.connect(host='localhost',
                        port = 3306,
                        user = 'root',
                        password = 'root',
                        database = 'test',
                        charset = 'utf8mb4'
                        )

        # 创建游标
        self.cursor = self.conn.cursor()
 
    def process_item(self,item,spider):

        # movie_name = item['movie_name']
		# movie_types = item['movie_types']
		# movie_release = item['movie_release']

        # sql语句
        insert_sql = """
        insert into movie(movie_name,movie_type,movie_release) VALUES(%s,%s,%s)
        """
        
        try:
            # 执行插入数据到数据库操作
            self.cursor.execute(insert_sql,(item['movie_name'],item['movie_types'],item['movie_release']))
            # 提交，不进行提交无法保存到数据库
            self.conn.commit()
        except Exception:
            print('执行sql语句异常',Exception)
        finally:
            pass

        return item
 
    def close_spider(self,spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()

 
