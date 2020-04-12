import requests 
from lxml import etree

def get_data():
    url = "https://www.jianshu.com/p/18ddd53cd3c0"
    headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36"
        }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    response = response.text
    code = etree.HTML(response)
    result = code.xpath('//div[@class="note"]//text()')
    img = code.xpath('//div[@class="image-view"]/img/@data-original-src')
    print(img)
    arr = ''
    for item in result:
        arr += item
    with open("./语法基础/res/文章test11.txt", "w") as f:
        f.write(arr)

def get_data1():
    url = "https://news.china.com/domestic/945/20200411/38060954.html"
    # headers = {
    #         "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) "
    #         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36"
    #     }
    content = requests.get(url).content
    code = etree.HTML(content)
    result = code.xpath('//div[@id="chan_newsDetail"]//text()')
    print(result)
    # arr = ''
    # for item in result:
    #     arr += item.replace('\n', '')
    # with open("./语法基础/res/文章1.txt", "w") as f:
    #     f.write(arr)

if __name__ == '__main__':
    get_data()
