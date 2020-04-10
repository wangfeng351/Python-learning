"""
python数据分组练习
@Date 2020.04.09
"""
from itertools import groupby
students = [{'name': '老颜', 'age': '20'},
            {'name': '老吴', 'age': '19'},
            {'name': '老席', 'age': '19'},
            {'name': '老王', 'age': '21'},
            {'name': '恋姐', 'age': '24'}]
# 分组前没有按照分组字段排序，分组失败
for k, items in groupby(students, key=lambda x: x['age']):
    print(k)
    for i in items:
        print(i)

print('****************************************************')

# 分组前按照分组字段排序， 分组成功
students.sort(key=lambda  x: x['age'])
for k, items in groupby(students, key=lambda x: x['age']):
    print(k)
    for i in items:
        print(i)