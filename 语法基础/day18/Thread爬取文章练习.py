from time import time
from threading import Thread
from lxml import etree

import requests
# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):
    # 全参构造函数
    def __init__(self, url, index):
        super().__init__()
        self.url = url
        self.index = index
    def run(self):
        # 根据网页地址获取网页源码，字符串格式
        content = requests.get(self.url).content
        # 将获取的源码转为html格式
        code = etree.HTML(content)
        # 获取节点，text()为获取该节点下的内容
        result = code.xpath('//div[@id="chan_newsDetail"]//text()')
        # 获取图片的src属性
        img = code.xpath('//p[@class="f_center pcenter"]/img/@src')
        print(img)
        # 将网页文本内容存入txt文件中
        arr = ''
        for item in result:
            arr += item + "\n"
        with open("./语法基础/res/文章" + str(self.index) + ".txt", "w") as f:
            f.write(arr)

def main():
    # 使用了天下数据接口提供的网络API, 用自己的key替换掉下面代码中的APIKey即可
    resp = requests.get(
        'http://api.tianapi.com/allnews/index?key=40d6c1374b33ddaa3e95ae07bb12af7c&num=10&col=7')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    index = 0
    # 通过newslist关键字得到newslist中的数据
    for mm_dic in data_model['newslist']:
        index +=1
        # 获取url
        url = mm_dic['url']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url, index).start()

if __name__ == '__main__':
    main()