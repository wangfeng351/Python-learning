"""
字典创建方法
@Date 2020.05.05
"""

# 5种创建方法，注意dict是关键词，所有变量名取得是dic
# 1. 手动创建
empty = {}
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic)
# 2. 使用dict()构造函数
dict(a=1, b=2, c=3)
print(dic)
# 3. 键值对+关键字参数
dict({'a': 1, 'b': 2}, c=3, d=4)
print(dic)
# 4. 可迭代对象，列表，元素又为一个元组，后面再加一系列关键字参数
dict([('a', 1), ('b', 2)], c=3)
print(dic)
# 5. fromkeys()方法
dic = {}.fromkeys(['k1', 'k2', 'k3'], [1,2,3])
print(dic)