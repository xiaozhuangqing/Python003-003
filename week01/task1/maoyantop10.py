
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 获得前10个电影的链接
def get_movies_url(URL):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

    header = {'user-agent':user_agent}
    response = requests.get(URL,headers=header)
    bs_info = bs(response.text,'html.parser')

    urls = []
    for tags in bs_info.find_all('div', attrs={'class':'channel-detail movie-item-title'},limit=10):
        for atag in tags.find_all('a',):
            urls.append(f'https://maoyan.com' + atag.get('href'))
    return urls
    


# 获取电影的名称，类型，上映时间
def moviesinfo(urls):
    mylist = []
    for url in urls:
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        header = {'user-agent':user_agent}
        response = requests.get(url,headers=header)
        bs_info = bs(response.text,'html.parsr')

        #电影名称
        movier_name = bs_info.find('h1',attrs={'class':'name'}).text
        #类型
        movie_type_list = bs_info.find_all('a',attrs={'class':'text-link'})
        movie_types = ''
        for movie_type in movie_type_list:
            movie_types +=movie_type.text

        #上映时间
        movie_release = bs_info.find_all('li',attrs={'class':'ellipsis'})

        info_list = [movier_name,movie_types,movie_release]
        mylist.append(info_list)


URL = 'https://maoyan.com/films?catId=3&showType=3'
#获取电影链接
urls = get_movies_url(URL)
#获取电影详情并保存本地文件
movie_data = pd.DataFrame(moviesinfo(urls))
movie_data.to_cvs('./task1/movies.cvs',encoding='utf8',index=False,header=False)
