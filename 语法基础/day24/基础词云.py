"""
基础词云
@Date 2020.04.17
"""
import wordcloud
import random

# 创建词云对象
w = wordcloud.WordCloud()
# 通过字符串生成词云
w.generate('From tomorrow on, be a happy man.Feed horses, chop wood, travel the world.\
    From tomorrow on, care about food and vegetables. I have a house, facing the sea, spring flowers.')
# 生成本地图片
w.to_file('./语法基础/res/image/output.png')


# 创建词云对象，设置词云图片宽，高，字体，背景颜色等参数
# 中文字体需要提前下载文字文件
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='#eeeeee',
                        font_path='./语法基础/res/font/SimHei.ttf')
w.generate('会当凌绝顶，一览众山小')
w.to_file('./语法基础/res/image/output2.png')
