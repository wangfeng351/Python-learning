import  requests
import urllib.parse
import base64
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
import json
header={
        'Host':'music.163.com',
        'content-lenth':'472',
        'Cache-Control':'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        #'Cookie':'iuqxldmzr_=32; _ntes_nnid=a6f29f40998c88c693bc910331bd6bea,1558011234325; _ntes_nuid=a6f29f40998c88c693bc910331bd6bea; _ga=GA1.2.2120707788.1559308501; WM_TID=pV2C%2BjTrRwBBAAERUVJojniTwk8%2B8Zta; JSESSIONID-WYYY=nvf%2BggodQRfcT%2BTvBRmANqMrsDeQCxRvqwFsxDr3eJvNNWhGYFhfCXKFkfAfOdbHhpCsMzT39mAeJ7ZamBQZbiwwtnSZD%5CPWRqKxD9t6dGKD3bTVjomjgB39DB07RNIWI32bYKa2H4fg1qQgqI%2FR%2B%2Br%2BZXJvgFg1Vh%2FA2XRj9S4p0EMu%3A1560927288799; WM_NI=DthwcEQf5Ew2NbTIZmSNhSnm%2F8VWsg5RxhkYogvs2luEwZ6m5UhdzbHYPIr654ZBWKV4o22%2BEwb9BvdLS%2BFOmOAEUG%2B8xd8az4CX%2FiAL%2BZkz3syA0onCPkhQwCtL4pkUcjg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed2d650989c9cd1dc4bb6b88eb2c84e979f9aaff773afb6fb83d950bcb19ecce92af0fea7c3b92a88aca898e24f93bafba6f63a8ebe9caad9679192a8b4ed67ede89ab8f26df78eb889ea53adb9ba94b168b79bb9bbb567f78ba885f96a8c87a0aaf13ef7ec96a3d64196eca1d3b12187a9aedac17ea8949dccc545af918fa6d84de9e8b885bb6bbaec8db9ae638394e5bbea72f1adb7a2b365ae9da08ceb5bb59dbcadb77ca98bad8be637e2a3'
        }

def pkcs7padding(text):
    """
    明文使用PKCS7填充
    最终调用AES加密方法时，传入的是一个byte数组，要求是16的整数倍，因此需要对明文进行处理
    :param text: 待加密内容(明文)
    :return:
    """
    bs = AES.block_size  # 16
    length = len(text)
    bytes_length = len(bytes(text, encoding='utf-8'))
    # tips：utf-8编码时，英文占1个byte，而中文占3个byte
    padding_size = length if(bytes_length == length) else bytes_length
    padding = bs - padding_size % bs
    # tips：chr(padding)看与其它语言的约定，有的会使用'\0'
    padding_text = chr(padding) * padding
    return text + padding_text
def encrypt(key, content):
    """
    AES加密
    key,iv使用同一个
    模式cbc
    填充pkcs7
    :param key: 密钥
    :param content: 加密内容
    :return:
    """
    key_bytes = bytes(key, encoding='utf-8')
    iv = bytes('0102030405060708', encoding='utf-8')
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
    # 处理明文
    content_padding = pkcs7padding(content)
    # 加密
    encrypt_bytes = cipher.encrypt(bytes(content_padding, encoding='utf-8'))
    # 重新编码
    result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
    return result
def getcomment(songid,page):
    url="https://music.163.com/weapi/v1/resource/comments/R_SO_4_"+songid+"?csrf_token="
    # print(url)
    formdata = {
        "params": "",
        "encSecKey": "c81160c64a08feb6cfed91c1619d5bffd05dd278b685c94a748689edf035ee0436b66aa7019927ce0fedd26aee9a22cdc6743e58a120f9db0126ebb2e61dae3f7ee21088eb747f829bceed9a5bbb9ee7a2eecf1a358feac431acaab17c95b8491a6a955f7c17a02a3e7886390c2cb3b981f4ccbd5163a566d27ace95db073401",
    }

    aes_key = '0CoJUm6Qyw8W8jud'## 不变的
    # print('aes_key:' + aes_key)
    # 对英文加密
    source_en = '{"rid":"R_SO_4_'+songid+'","offset":"'+str(page*100)+'","total":"false","limit":"100","csrf_token":""}'

    #offset自己该
    # print(source_en)
    encrypt_en = encrypt(aes_key, source_en)#第一次加密
    # print(encrypt_en)
    aes_key='3Unu7SzdXGctW1vA'
    encrypt_en = encrypt(aes_key, str(encrypt_en))  # 第二次加密
    # print(encrypt_en)
    formdata['params']=encrypt_en
    # print(formdata['params'])
    formdata = urllib.parse.urlencode(formdata).encode('utf-8')
    # print(formdata)
    req = requests.post(url=url, data=formdata, headers=header)
    return req.json()
if __name__ == '__main__':
    songid='1405283464'
    page=0
    text=''
    list = []
    for page in range(0, 30):
        comment=getcomment(songid,page)
        print(len(comment['comments']) + page)
        list.append(comment['comments'])
    with open('./语法基础/res/json/句号.json', 'w') as fs:
        json.dump(list, fs,  ensure_ascii=False)