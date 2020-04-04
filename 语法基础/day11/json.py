"""
requests请求api, 用字典和列表保存为json
"""

import json
import requests
resp = requests.get(
    'http://api.tianapi.com/allnews/index?key=40d6c1374b33ddaa3e95ae07bb12af7c&num=10&col=7')
newslist = json.loads(resp.text)['newslist']
result = []
data = 'data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['title'] = news['title']
    temp_dict['pic_url'] = news['picUrl']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f)