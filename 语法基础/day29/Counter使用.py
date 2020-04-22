"""
Counter使用
@Date 2020.04.22
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "dont't", 'look', 'around', 'the', 'eyes', 
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
# 找出序列中出现次数最多的元素
print(counter.most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
# elements() 按照counter的计数，重复返回元素
list = list(c.elements())
print(list)