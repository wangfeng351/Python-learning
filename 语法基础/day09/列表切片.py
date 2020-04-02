"""
列表切片
Date: 2020.4.2

"""
fruits = ['apple', 'caomei', 'tomato', 'banana']
fruits += ['mango', 'pear', 'potato']
# 列表切片
fruits2 = fruits[1:4]
# ['caomei', 'tomato', 'banana']
print(fruits2)
# 可以通过完整切片操作来赋值列表
fruits3 = fruits[:]
# ['apple', 'caomei', 'tomato', 'banana' ,'mango', 'pear', 'potato']
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4) # ['mango', 'pear']
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
# ['potato', 'pear', 'mango', 'banana', 'tomato', 'caomei', 'apple']
print(fruits5)

