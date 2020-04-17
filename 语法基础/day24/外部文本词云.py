"""
外部文本词云
@Date 2020.04.17
"""

import wordcloud
import random

# 读入外部文本文件
f = open('./语法基础/res/text/wf.txt', encoding='utf-8')
txt = f.read()
# 更换一下背景颜色和整体风格
# colormap参考 https://matplotlib.org/examples/color/colormaps_reference.html
w = wordcloud.WordCloud(
    scale=1.5,
    max_font_size=120,
    background_color='#a9ded2',
    colormap = 'summer',
    font_path='./语法基础/res/font/SimHei.ttf')

# 将txt变量传入
w.generate(txt)
w.to_file('./语法基础/res/image/output4.png')