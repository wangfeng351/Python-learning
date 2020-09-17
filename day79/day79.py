"""
快速读取文件内容
2020.9.16
"""
# 只读方式打开本地文件, res目录
f = open("语法基础/res/text/文章1.txt", "r")
# 读取全部内容，并以列表形式全部返回
lines = f.readlines()
# for循环遍历列表，每次输出一行
for line in lines:
    print(line)
# 关闭文件
f.close