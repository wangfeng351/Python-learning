"""
中文文本的情感分析
@Date 2020.04.28
"""

from snownlp import SnowNLP

text = '感情中最容易出现的问题是，不懂得珍惜当下，只有失去之后才明白珍惜的道理。'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断， 返回值为正面情绪的概率，越接近1表示正面情绪，越接近0表示负面情绪
text1 = '今天真倒霉'
text2 = '还好，今天不算太倒霉'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
# 这部电影真心棒0.9
print(text1, s1.sentiments)
# 这部电影简直烂到爆
print(text2, s2.sentiments)

#关键字抽取
text3 = '没有梦想的人生是不完美的，实现了的梦想，又是那么的平常、淡淡和恬静，但却是真实的人生，是值得回味的人生。 '
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
# 概况总结文字
print(s3.summary(limit=4))