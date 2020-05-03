"""
List基本操作
@Date 2020.05.03
"""
# 创建
empty = []
lst = [1, 'xiaoming', 29.5, '14752191369']
lst2 = ['001', '2019-11-11', ['三文鱼', '羊肉串']]
# 长度
print(len(lst2))
# 遍历
for _ in lst:
    print(f'{_}的类型位{type(_)}')

# 插入删除等操作
sku = lst2[2]
# append追加到lst尾部
sku.append('烤鸭')
# insert到指定索引处
sku.insert(1, '烤面筋')
# pop移除尾部元素
item = sku.pop()
# remove移除, 或者sku.remove(sku[0])
sku.remove('三文鱼')
print(sku)

# 生成1到20的序列， 步长为3，放入list
a = list(range(1, 20, 3))
print(a)
# 各种切片操作
print(a[-1], a[:-1], a[1:5], a[1:5:2], a[::3], a[::-3])