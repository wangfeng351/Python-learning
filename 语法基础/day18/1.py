import requests 
from lxml import etree

def get_data():
    url = "https://news.china.com/domestic/945/20200411/38060954.html"
    headers = {
            "User-Agent": 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T)'
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36'
        }
    response = requests.get(url, headers=headers)
    result = response.content.decode("utf8","ignore").encode("gbk","ignore")
    print(result)
    # code = etree.HTML(response)
    # result = code.xpath('//div[@class="note"]//text()')
    # print(result)

if __name__ == '__main__':
    get_data()
