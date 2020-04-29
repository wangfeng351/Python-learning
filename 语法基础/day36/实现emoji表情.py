"""
使用python实现emoji表情
@Date 2020.04.29
"""
import emoji

# 
print(emoji.emojize(''))
# 有些特殊的表情需要指定 use_aliases=True 参数才可以实现
# Sleeping is
print(emoji.emojize('Please care about yourself sister mq', use_aliases=True))
# 可以单词形式
print(emoji.emojize('你是猪吗？ Under such great pressure every day！！！'))
# 也可以用unicode形式
print(emoji.emojize('\U0001F32D'), emoji.emojize('\U0001F354'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'))
print(emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'))
print(emoji.emojize('\U0001F497'), emoji.emojize('\U0001F496'),
      emoji.emojize('\U0001F495'), emoji.emojize('\U0001F497'),
      emoji.emojize('\U0001F496'), emoji.emojize('\U0001F495'))