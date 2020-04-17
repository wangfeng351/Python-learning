# 导入词云制作库worldcloud和中文分词库jieba
import jieba
import wordcloud
# 构建并配置词云对象w
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#egdfds',
    colormap='',
    font_path='./语法基础/res/font/SimHei.ttf')

txt = '天将降大任于斯人也，必先苦其心志，劳其筋骨，饿其体肤，方可成大才。'
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)

# 将词云图片导出到当前文件夹
w.generate(string)

# 将词云图片导出到当前文件夹
w.to_file('./语法基础/res/image/output5.png')