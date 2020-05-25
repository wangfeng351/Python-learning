"""
Numpy_3
@Date 2020.05.25
"""

import numpy as np
v1 = np.arange(5)
print('输出v1:')
print(v1)
# 按照元素顺序逐个加2
print('输出v1*v1')
print(v1*v1)
# 
v2 = np.random.randint(1, 10, (5, 2))
print('v2')
print(v2)
# 此时无法直接将两个矩阵相乘，why？
# print(v1 * v2)
# 1. 使用dto函数实现矩阵乘法，自己运算验证
v3 = np.dot(v1, v2)
print('输出dot函数实训矩阵相乘结果')
print(v3)
# 输出矩阵的“形状”，也就是行列维度
print('输出v3的shape')
print(v3.shape)
# 2. 转化为matrix， 对象， 在相乘
v3 = np.matrix(v1)*np.matrix(v2)
print('输出使用matrix实现的矩阵相乘结果')
print(v3)