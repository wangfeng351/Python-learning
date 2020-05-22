"""
那些操作
@Date 2020.05.22
"""
# 字符串处理成字典
s = 'k0:10|k1:2|k2:11|k3:5'
m = map(lambda x: x.split(':'), s.split('|'))
print({mi[0]: int(mi[1]) for mi in m})

# 使用filter()求出列表中大于10的元素
a = [15, 2,7,20,400,10,9,-15,107]
b = list(filter(lambda x: x>10, a))
print(b)

# 列表内元素可重复出现, 如何删除列表中的某个元素
def del_item(lst,e):
    for i in lst:
        if i == e:
            lst.remove(i)
    return lst

s = del_item([1,3,5,3,2], 3)
print(s)
# 上述代码好像成功删除了元素3，可是。。。看下面
s = del_item([1,3,3,3,5], 3)
print(s)

def del_itme2(lst,e):
    i = 0
    while i < len(lst):
        while i < len(lst):
            if lst[i] == e:
                lst.remove(lst[i])
            else:
                i+=1
        return lst
# 再次调用看结果
s = del_itme2([1,2,2,2,5], 3)
print(s)