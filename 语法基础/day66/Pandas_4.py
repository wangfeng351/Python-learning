"""
Pandas_4
"""
import pandas as pd
import numpy as np
# 创建 DataFrame 的常用方法
df1 = pd.DataFrame([['yzh', 86.0, '2000-05-01'],
                    ['wjh', 91.5, '2000-06-01']],
                   index=['a', 'b'],
                   columns=['name', 'score', 'date'])
print(df1)
# 也可以通过字典
df2 = pd.DataFrame({'name': ['xu', 'wang'], 'score': [87, 98],
                    'date': ['1999-05-01', '1999-06-01']}, index=['x', 'y'])
print(df2)
# DataFrame增加数据
df2 = df2.append(pd.Series(
    data=['wang', 93, '2020-02-01'], index=['name', 'score', 'date'], name='x'
))
print(df2)
# DataFrame 删除数据，使用drop删除指定索引或标签，删除副本
df2 = df2.drop('x')
print(df2)
# DataFrame 修改数据，先根据索引或标签定位到行列再修改
df1.loc['a', 'name'] = 'new name'
print(df1)
# Pandas 推荐使用访问接口 iloc（索引访问）、loc(标签访问) 访问数据
print(df1.iloc[1, :])
print(df1.loc['b', 'name'])