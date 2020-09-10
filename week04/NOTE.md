学习笔记

第四周 《数据清洗与预处理》

本周课程老师举了一个生动的例子，结合前三周学习的Scrapy，如果说我们是在烹饪做菜，那么学习Scrapy就是去菜场挑选我们需要的食材，接下来就是洗菜烹饪，这便是我们这周学的内容

pandas
是一个开源的，BSD许可的库，为Python编程语言提供高性能，易于使用的数据结构和数据分析工具。

Pandas解决了什么问题？
Python在数据处理和准备方面一直做得很好，但在数据分析和建模方面就没那么好了。Pandas帮助填补了这一空白，使您能够在Python中执行整个数据分析工作流程，而不必切换到更特定于领域的语言，如R。

与出色的 IPython 工具包和其他库相结合，Python中用于进行数据分析的环境在性能、生产率和协作能力方面都是卓越的。

Pndas 适用于处理以下类型的数据：

与 SQL 或 Excel 表类似的，含异构列的表格数据;
有序和无序（非固定频率）的时间序列数据;
带行列标签的矩阵数据，包括同构或异构型数据;
任意其它形式的观测、统计数据集, 数据转入 Pandas 数据结构时不必事先标记。
Pandas 的主要数据结构是 Series（一维数据）与 DataFrame（二维数据），这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数典型用例。对于 R 用户，DataFrame 提供了比 R 语言 data.frame 更丰富的功能。Pandas 基于 NumPy 开发，可以与其它第三方科学计算支持库完美集成。

Pandas 就像一把万能瑞士军刀，下面仅列出了它的部分优势 ：

处理浮点与非浮点数据里的缺失数据，表示为 NaN；
大小可变：插入或删除 DataFrame 等多维对象的列；
自动、显式数据对齐：显式地将对象与一组标签对齐，也可以忽略标签，在 Series、DataFrame 计算时自动与数据对齐；
强大、灵活的分组（group by）功能：拆分-应用-组合数据集，聚合、转换数据；
把 Python 和 NumPy 数据结构里不规则、不同索引的数据轻松地转换为 DataFrame 对象；
基于智能标签，对大型数据集进行切片、花式索引、子集分解等操作；
直观地合并（merge）、**连接（join）**数据集；
灵活地重塑（reshape）、**透视（pivot）**数据集；
轴支持结构化标签：一个刻度支持多个标签；
成熟的 IO 工具：读取文本文件（CSV 等支持分隔符的文件）、Excel 文件、数据库等来源的数据，利用超快的 HDF5 格式保存 / 加载数据；
时间序列：支持日期范围生成、频率转换、移动窗口统计、移动窗口线性回归、日期位移等时间序列功能。andas 适用于处理以下类型的数据：

与 SQL 或 Excel 表类似的，含异构列的表格数据;
有序和无序（非固定频率）的时间序列数据;
带行列标签的矩阵数据，包括同构或异构型数据;
任意其它形式的观测、统计数据集, 数据转入 Pandas 数据结构时不必事先标记。
Pandas 的主要数据结构是 Series（一维数据）与 DataFrame（二维数据），这两种数据结构足以处理金融、统计、社会科学、工程等领域里的大多数典型用例。对于 R 用户，DataFrame 提供了比 R 语言 data.frame 更丰富的功能。Pandas 基于 NumPy 开发，可以与其它第三方科学计算支持库完美集成。

Pandas 就像一把万能瑞士军刀，下面仅列出了它的部分优势 ：

处理浮点与非浮点数据里的缺失数据，表示为 NaN；
大小可变：插入或删除 DataFrame 等多维对象的列；
自动、显式数据对齐：显式地将对象与一组标签对齐，也可以忽略标签，在 Series、DataFrame 计算时自动与数据对齐；
强大、灵活的分组（group by）功能：拆分-应用-组合数据集，聚合、转换数据；
把 Python 和 NumPy 数据结构里不规则、不同索引的数据轻松地转换为 DataFrame 对象；
基于智能标签，对大型数据集进行切片、花式索引、子集分解等操作；
直观地合并（merge）、**连接（join）**数据集；
灵活地重塑（reshape）、**透视（pivot）**数据集；
轴支持结构化标签：一个刻度支持多个标签；
成熟的 IO 工具：读取文本文件（CSV 等支持分隔符的文件）、Excel 文件、数据库等来源的数据，利用超快的 HDF5 格式保存 / 加载数据；
时间序列：支持日期范围生成、频率转换、移动窗口统计、移动窗口线性回归、日期位移等时间序列功能。


数据结构
维数	名称	描述
1	Series	带标签的一维同构数组
2	DataFrame	带标签的，大小可变的，二维异构表格
#为什么有多个数据结构？
Pandas 数据结构就像是低维数据的容器。比如，DataFrame 是 Series 的容器，Series 则是标量的容器。使用这种方式，可以在容器中以字典的形式插入或删除对象。

此外，通用 API 函数的默认操作要顾及时间序列与截面数据集的方向。多维数组存储二维或三维数据时，编写函数要注意数据集的方向，这对用户来说是一种负担；如果不考虑 C 或 Fortran 中连续性对性能的影响，一般情况下，不同的轴在程序里其实没有什么区别。Pandas 里，轴的概念主要是为了给数据赋予更直观的语义，即用“更恰当”的方式表示数据集的方向。这样做可以让用户编写数据转换函数时，少费点脑子。

处理 DataFrame 等表格数据时，index（行）或 columns（列）比 axis 0 和 axis 1 更直观。用这种方式迭代 DataFrame 的列，代码更易读易懂：

# # 从列表创建Series
# pd.Series(['a', 'b', 'c'])
# # 0    a
# # 1    b
# # 2    c
# # dtype: object
# # 自动创建索引

# # 通过字典创建带索引的Series
# s1 = pd.Series({'a':11, 'b':22, 'c':33})
# # 通过关键字创建带索引的Series
# s2 = pd.Series([11, 22, 33], index = ['a', 'b', 'c'])
# s1
# s2

# # 获取全部索引
# s1.index
# # 获取全部值
# s1.values

# # 类型
# type(s1.values)    # <class 'numpy.ndarray'>
# type(np.array(['a', 'b']))

# # 转换为列表
# s1.values.tolist()

# # 使用index会提升查询性能
# #    如果index唯一，pandas会使用哈希表优化，查询性能为O(1)
# #    如果index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)
# #    如果index完全随机，每次查询都要扫全表，查询性能为O(N)

# # 取出email
# emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
# import re
# pattern ='[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
# mask = emails.map(lambda x: bool(re.match(pattern, x)))

#---------------------------------------------------------------
# import pandas as pd


# # 列表创建dataframe
# df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
# # 嵌套列表创建dataframe
# df2 = pd.DataFrame([
#                      ['a', 'b'],
#                      ['c', 'd']
#                     ])
# # 自定义列索引
# df2.columns= ['one', 'two']
# # 自定义行索引
# df2.index = ['first', 'second']

# df2
# # 可以在创建时直接指定 DataFrame([...] , columns='...', index='...' )


pandas 数据导入
# # 导入excel文件
# excel1 = pd.read_excel(r'1.xlsx')
# excel1
# # 指定导入哪个Sheet
# pd.read_excel(r'1.xlsx',sheet_name = 0)

# # 支持其他常见类型
# pd.read_csv(r'c:\file.csv',sep=' ', nrows=10, encoding='utf-8')

# pd.read_table( r'file.txt' , sep = ' ')


# import pymysql
# sql  =  'SELECT *  FROM mytable'
# conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
# df = pd.read_sql(sql,conn)


pandas数据处理

# x = pd.Series([ 1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])
# #检验序列中是否存在缺失值
# x.hasnans

# # 将缺失值填充为平均值
# x.fillna(value = x.mean())

# # 前向填充缺失值

# df3=pd.DataFrame({"A":[5,3,None,4],
#                  "B":[None,2,4,3],
#                  "C":[4,3,8,5],
#                  "D":[5,4,2,None]})

# df3.isnull().sum() # 查看缺失值汇总
# df3.ffill() # 用上一行填充
# df3.ffill(axis=1)  # 用前一列填充

# # 缺失值删除
# df3.info()
# df3.dropna()

# # 填充缺失值
# df3.fillna('无')

# # 重复值处理
# df3.drop_duplicates()

# # 行列调整
# df = pd.DataFrame({"A":[5,3,None,4],
#                  "B":[None,2,4,3],
#                  "C":[4,3,8,5],
#                  "D":[5,4,2,None]})

# df2 = pd.DataFrame({"A":[5,3,None,5],
#                  "B":[None,2,4,3],
#                  "C":[4,3,8,5],
#                  "D":[5,4,2,None]})

# # 列的选择,多个列要用列表
# df[ ['A', 'C'] ]

# # 某几列
# df.iloc[:, [0,2]] # :表示所有行，获得第1和第3列

# # 行选择
# df.loc[ [0, 2] ] # 选择第1行和第3行
# df.loc[ 0:2    ] # 选择第1行到第3行

# # 比较
# df[ ( df['A']<5 ) & ( df['C']<4 )   ]

# 数值替换

# 一对一替换
# 用于单个异常值处理
# df['C'].replace(4,40)

# import numpy as np
# df.replace(np.NaN, 0)

# # 多对一替换
# df.replace([4,5,8], 1000)

# # 多对多替换
# df.replace({4:400,5:500,8:800})

# # 排序
# # 按照指定列降序排列
# df.sort_values ( by = ['A'] ,ascending = False)

# # 多列排序
# df.sort_values ( by = ['A','C'] ,ascending = [True,False])


# # 删除
# # 删除列
# df.drop( 'A' ,axis = 1)

# # 删除行
# df.drop( 3 ,axis = 0)

# # 删除特定行
# df [  df['A'] < 4 ]

# # 行列互换
# df.T
# df.T.T

# # 索引重塑
# df4 = pd.DataFrame([
#                      ['a', 'b', 'c'],
#                      ['d', 'e', 'f']
#                     ],
#                     columns= ['one', 'two', 'three'],
#                     index = ['first', 'second']
#                    )
# df4.stack()
# df4.unstack()
# df4.stack().reset_index()

#---------------------------------------------------------------

# import pandas as pd
# df = pd.DataFrame({"A":[5,3,None,4],
#                  "B":[None,2,4,3],
#                  "C":[4,3,8,5],
#                  "D":[5,4,2,None]})
# # 算数运算
# # 两列之间的加减乘除
# df['A'] + df['C']

# # 任意一列加/减一个常数值，这一列中的所有值都加/减这个常数值
# df['A'] + 5

# # 比较运算
# df['A'] > df ['C']

# # count非空值计数
# df.count()

# # 非空值每列求和
# df.sum()
# df['A'].sum()

# # mean求均值
# # max求最大值
# # min求最小值
# # median求中位数
# # mode求众数
# # var求方差
# # std求标准差

#---------------------------------------------------------------
# import pandas as pd
# import numpy as np

# # 聚合
# sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
#          {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
#          {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]

# df2 = pd.DataFrame(sales)
# df2.groupby('type').groups

# for a, b in df2.groupby('type'):
#     print(a)
#     print(b)

# # 聚合后再计算
# df2.groupby('type').count()
# # df2.groupby('Jan').sum()


# # 各类型产品的销售数量和销售总额
# df2.groupby('type').aggregate( {'type':'count' , 'Feb':'sum' })


# group=['x','y','z']
# data=pd.DataFrame({
#     "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
#     "salary":np.random.randint(5,50,10),
#     "age":np.random.randint(15,50,10)
#     })


# data.groupby('group').agg('mean')
# data.groupby('group').mean().to_dict()
# data.groupby('group').transform('mean')

# # 数据透视表
# pd.pivot_table(data,
#                values='salary',
#                columns='group',
#                index='age',
#                aggfunc='count',
#                margins=True
#             ).reset_index()

#---------------------------------------------------------------
# import pandas as pd
# import numpy as np

# group = ['x','y','z']
# data1 = pd.DataFrame({
#     "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
#     "age":np.random.randint(15,50,10)
#     })

# data2 = pd.DataFrame({
#     "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
#     "salary":np.random.randint(5,50,10),
#     })

# data3 = pd.DataFrame({
#     "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
#     "age":np.random.randint(15,50,10),
#     "salary":np.random.randint(5,50,10),
#     })

# # 一对一
# pd.merge(data1, data2)

# # 多对一
# pd.merge(data3, data2, on='group')

# # 多对多
# pd.merge(data3, data2)

# # 连接键类型，解决没有公共列问题
# pd.merge(data3, data2, left_on= 'age', right_on='salary')

# # 连接方式
# # 内连接，不指明连接方式，默认都是内连接
# pd.merge(data3, data2, on= 'group', how='inner')
# # 左连接 left
# # 右连接 right
# # 外连接 outer

# # 纵向拼接
# pd.concat([data1, data2])

#---------------------------------------------------------------
# import pandas as pd
# import numpy as np

# dates = pd.date_range('20200101', periods=12)
# df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))
# df

# #                    A         B         C         D
# # 2020-01-01  0.046485 -0.556209  1.062881 -1.174129
# # 2020-01-02  1.066051 -0.343081  1.054913  1.601051
# # 2020-01-03  0.191064 -0.386905  0.516403  0.259818
# # 2020-01-04 -0.168462 -1.488041 -0.457658  0.913574
# # 2020-01-05 -0.502614  1.235633 -0.578284 -0.362737
# # 2020-01-06 -0.193310  0.652285 -0.346359  0.347364
# # 2020-01-07  2.308562 -0.679108  0.856449  0.490840
# # 2020-01-08  0.871489  0.338133 -0.163669  0.300147
# # 2020-01-09 -1.245250  0.667357 -1.287782  1.494880
# # 2020-01-10  0.387925 -1.058867 -0.397298  0.514921
# # 2020-01-11 -0.440884  0.904307  1.338720  0.612919
# # 2020-01-12 -0.864941 -0.358934 -0.203868 -1.191186

# import matplotlib.pyplot as plt
# plt.plot(df.index, df['A'], )
# plt.show()

# plt.plot(df.index, df['A'],
#         color='#FFAA00',    # 颜色
#         linestyle='--',     # 线条样式
#         linewidth=3,        # 线条宽度
#         marker='D')         # 点标记

# plt.show()

# # seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观
# import seaborn as sns
# # 绘制散点图
# plt.scatter(df.index, df['A'])
# plt.show()

# # 美化plt
# sns.set_style('darkgrid')
# plt.scatter(df.index, df['A'])
# plt.show()

#---------------------------------------------------------------


