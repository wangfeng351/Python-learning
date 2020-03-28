"""
生成斐波那契数的前20个数
"""

x = 1
y = 1
z = 0
print(x, ',', y, end='')
for i in range(3, 21):
    z = x + y
    print(',', z, end='')
    x = y
    y = z
print()