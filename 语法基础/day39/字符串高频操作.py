"""
字符串高频操作
@Date 2020.05.02
"""

# re为正则表达式库
import re
# strip 用于取出字符串前后的空格
print(' I love python and Java\t\n '.strip())
# replace 用于字符串的替换
print('I Love Python'.replace(' ', '_'))
# join用于合并字符串
print('_'.join(['book', 'store', 'count']))
# title 用于单词的首字母大写
print('i love python'.title())
# find 用于返回匹配字符串的起始位置索引
print('i love python'.find('python'))

# 正则
# 密码安全登录请求， 6到12位，包含英文字母和数字
# 方法： \da-zA-Z 满足“密码只包含英文字母和数字”
# \d匹配数字0-9
# a-z 匹配所有小写字母： A-Z匹配所有大写字母
# 通用最保险的 fullmatch 方法， 查看是否整个字符串都匹配
pat = re.compile(r'[\da-zA-Z]{6,12}')
print(pat.fullmatch('qaz12')) # 返回none, 长度低于6
print(pat.fullmatch('qaz123wsxedc43434')) # 返回none, 长度超过12
print(pat.fullmatch('qaz_231')) # 返回none， 含有下划线
print(pat.fullmatch('n0passwoRd'))  # 符合