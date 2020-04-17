import requests
from lxml import etree
import json
import pymysql
import time


headers = {
        'cookie': '_ntes_nnid=afc0b8c00fad7edac3529e13eb239079,1571915383131; _ntes_nuid=afc0b8c00fad7edac3529e13eb239079; __remember_me=true; WM_TID=YqM7BhU3VFBAVQBERUJ%2BUg%2Bozg%2BbhufE; MUSICIAN_COMPANY_LAST_ENTRY=316304066_musician; ntes_kaola_ad=1; WM_NI=8ccty8AYLgtKA5VvZoxNL9GiPnJnWaoCsUHIMlqs8rINtCNokTXpcogr2spFzUHcgOc0j82HgOTFATWvMUT%2FPegwi3Bd67p5xn00l2CrAO27Xrff%2B%2B76zJqs4cVDAtKJa1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed4fb7fb18a97d1e56bb19a8eb6c55b928b9baef15ead9afc82bb5ffcea96a9dc2af0fea7c3b92afcbdad95fc3483878488f74183eb9a97d965bc9284dac66394b2868fd66bad9dbdb6cb438fb4bf94bb7a8b92bca4cd65a98c9891e265a5aefe94f34eba8b8884e645a1f0a6d9b144a5919ca7c46095aa83b6d72594bba998ec3982bcfad8f33fbcb200d1ef3a81ae8fb0b13d9caeaa87aa21f5eab6abf479f8bd9aa5c4808996afd2d837e2a3; _iuqxldmzr_=33; JSESSIONID-WYYY=4vZFNPbaFcTomgzjs%2BZw3IXEtsZJU1zV9nXX2mJSys06YtWQNYC4EbHFjEO4Zhr05y5YpP087zMg7CJ0UQ%5CUOSF8z60xv6IGzsRzDy1NiBo8Xj157zfPUNIxX54jw1Vk685eMCXWDg6Tdu0u7NPFI45uCPf3PZTt2U60AAZZOqE6aHU%2B%3A1587102528986; playerid=55462361; MUSIC_U=ce1299bbfe2c8ced31eb76bf7c9a11bfcadf7a4d0478731a0d3bc96c04292f92f6dbb9e080384a87c20b862285ca8ec87955a739ab43dce1; __csrf=cd7bb5e8c6e740481ae96c662e06a751',
        'origin': 'https://music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'referer': 'https://music.163.com/m/discover/toplist?id=19723756',
    }

def get_song():
    url = 'https://music.163.com/weapi/v6/playlist/detail?csrf_token=cd7bb5e8c6e740481ae96c662e06a751'
    data = {
        'encSecKey': '4021383c6a8d10bc8d966c59bd8d1488a3535d5596c53d8e508ee5a540dc8179b70f8d3d0bb90b42a520325fc3085c2d3a1a203bc34b1b4f023e7043625f4ab4b6c93c8be855d83c7b438d9f15989b72f6b599a5c4cf922d616b39fcad8bb4a45c3b46669c7eb1e21409fddc79a973f570fc771972087f0664c7f57c4960aa7e',
        'params': 'a2w1fX1HEHrYHV/w5f0SCm/a/9fSTn2T9d3/iWk8vPV8DAdL2Mijjt3PNWSd3uLqBM32O7tu3MTy4Sy//BIk0K+tcc/P1jCdqe15WqMQK+Ir5UFbjIgxw1krdSd5YoI2g53EFtgIENw/IDWjpbtOT1uelUIkoIRlS7aTeSgNunPGipkt7lNilmTqsRigdMAV'
    }
    headers = {
        'cookie': '_ntes_nnid=afc0b8c00fad7edac3529e13eb239079,1571915383131; _ntes_nuid=afc0b8c00fad7edac3529e13eb239079; __remember_me=true; WM_TID=YqM7BhU3VFBAVQBERUJ%2BUg%2Bozg%2BbhufE; MUSICIAN_COMPANY_LAST_ENTRY=316304066_musician; ntes_kaola_ad=1; WM_NI=8ccty8AYLgtKA5VvZoxNL9GiPnJnWaoCsUHIMlqs8rINtCNokTXpcogr2spFzUHcgOc0j82HgOTFATWvMUT%2FPegwi3Bd67p5xn00l2CrAO27Xrff%2B%2B76zJqs4cVDAtKJa1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed4fb7fb18a97d1e56bb19a8eb6c55b928b9baef15ead9afc82bb5ffcea96a9dc2af0fea7c3b92afcbdad95fc3483878488f74183eb9a97d965bc9284dac66394b2868fd66bad9dbdb6cb438fb4bf94bb7a8b92bca4cd65a98c9891e265a5aefe94f34eba8b8884e645a1f0a6d9b144a5919ca7c46095aa83b6d72594bba998ec3982bcfad8f33fbcb200d1ef3a81ae8fb0b13d9caeaa87aa21f5eab6abf479f8bd9aa5c4808996afd2d837e2a3; _iuqxldmzr_=33; JSESSIONID-WYYY=4vZFNPbaFcTomgzjs%2BZw3IXEtsZJU1zV9nXX2mJSys06YtWQNYC4EbHFjEO4Zhr05y5YpP087zMg7CJ0UQ%5CUOSF8z60xv6IGzsRzDy1NiBo8Xj157zfPUNIxX54jw1Vk685eMCXWDg6Tdu0u7NPFI45uCPf3PZTt2U60AAZZOqE6aHU%2B%3A1587102528986; playerid=55462361; MUSIC_U=ce1299bbfe2c8ced31eb76bf7c9a11bfcadf7a4d0478731a0d3bc96c04292f92f6dbb9e080384a87c20b862285ca8ec87955a739ab43dce1; __csrf=cd7bb5e8c6e740481ae96c662e06a751',
        'origin': 'https://music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'referer': 'https://music.163.com/m/discover/toplist?id=19723756',
    }
    response = requests.post(url,data=data, headers=headers)
    with open('./语法基础/res/json/cloud.json', 'w') as fs:
        json.dump(response.json(), fs,  ensure_ascii=False)
    print(response.json())

def get_comment():
    url = 'https://music.163.com/weapi/v1/resource/comments/get?csrf_token=7cc132bc03a707b19829736d6fe2a5ee'
    data = {
        'encSecKey': '3b7be75ebabb52a546470f94bbe9f3434117c033c35df50016fb22ad0b10b8e0d66b90500580331be0ccea47a889225c2d7fc025052db1477f783d09e3d269b729263f36bc0afb1e9566a14e3d2892470725f1a816308f4e76b9e047d2f11541860c5a124fce5569e282a96690bba72ad11bbda7c5ad44b3fea87b8961e05375',
        'params': 'AK7WTSyZk8NObe+lk8Eb0McvqSDZvVn/maGkmIyp+objtXTQfuG9TFkC2rrC1cLaBjNoZ+VrABCsTO9GsuW1BaF/keDilEBTqy9/WU0/A7ilKK8fe7bOexlZJ1vuXZcIzUsJYDqnIefB+3iV/pW/6b6o5R52LzLcoh754+3IkafhsLy6/2/hOUSh2cpPIWSYrZjpD7irIC1OM7JOgXzHuPhCsh5fQl2CkRlTK0YXK4s='
    }
    headers = {
        'cookie': '_ntes_nnid=afc0b8c00fad7edac3529e13eb239079,1571915383131; _ntes_nuid=afc0b8c00fad7edac3529e13eb239079; __remember_me=true; WM_TID=YqM7BhU3VFBAVQBERUJ%2BUg%2Bozg%2BbhufE; MUSICIAN_COMPANY_LAST_ENTRY=316304066_musician; ntes_kaola_ad=1; WM_NI=8ccty8AYLgtKA5VvZoxNL9GiPnJnWaoCsUHIMlqs8rINtCNokTXpcogr2spFzUHcgOc0j82HgOTFATWvMUT%2FPegwi3Bd67p5xn00l2CrAO27Xrff%2B%2B76zJqs4cVDAtKJa1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed4fb7fb18a97d1e56bb19a8eb6c55b928b9baef15ead9afc82bb5ffcea96a9dc2af0fea7c3b92afcbdad95fc3483878488f74183eb9a97d965bc9284dac66394b2868fd66bad9dbdb6cb438fb4bf94bb7a8b92bca4cd65a98c9891e265a5aefe94f34eba8b8884e645a1f0a6d9b144a5919ca7c46095aa83b6d72594bba998ec3982bcfad8f33fbcb200d1ef3a81ae8fb0b13d9caeaa87aa21f5eab6abf479f8bd9aa5c4808996afd2d837e2a3; _iuqxldmzr_=33; JSESSIONID-WYYY=4vZFNPbaFcTomgzjs%2BZw3IXEtsZJU1zV9nXX2mJSys06YtWQNYC4EbHFjEO4Zhr05y5YpP087zMg7CJ0UQ%5CUOSF8z60xv6IGzsRzDy1NiBo8Xj157zfPUNIxX54jw1Vk685eMCXWDg6Tdu0u7NPFI45uCPf3PZTt2U60AAZZOqE6aHU%2B%3A1587102528986; playerid=55462361; MUSIC_U=ce1299bbfe2c8ced31eb76bf7c9a11bfcadf7a4d0478731a0d3bc96c04292f92f6dbb9e080384a87c20b862285ca8ec87955a739ab43dce1; __csrf=cd7bb5e8c6e740481ae96c662e06a751',
        'origin': 'https://music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'referer': 'https://music.163.com/m/discover/toplist?id=19723756',
    }
    response = requests.post(url,data=data, headers=headers)
    with open('./语法基础/res/json/comment.json', 'w') as fs:
        json.dump(response.json(), fs,  ensure_ascii=False)
    print(response.json())


def get_song_list_comment():
    for item in range(0, 1000, 100):
        url = 'http://music.163.com/api/v1/resource/comments/A_PL_0_19723756?limit=100' + '&offset=' + str(item)
        resp = requests.get(url, headers=headers)
        data = resp.json()
        insert_song_list_comment(data)
        insert_user(data)

def insert_song_list_comment(song_list_data):
    db = pymysql.connect("localhost", "root", "root", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_list_data['comments']:
        user = dic['user']
        user_item = (user['userId'],'123', user['nickname'], user['avatarUrl'],'2000-1-1 20:00:00', '2000-1-1 20:00:00')
        comment = (str(dic['commentId']), '19723756', str(user['userId']), dic['content'],dic['likedCount'], timeStamp(dic['time']), timeStamp(dic['time']))
        val.append(comment)
    with open('./语法基础/res/json/val.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = "INSERT INTO song_list_comment(id, song_list_id, user_id, comment_content, like_counts, create_time, update_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql,val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

def insert_user(song_list_data):
    db = pymysql.connect("localhost", "root", "root", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_list_data['comments']:
        userId = dic['user']['userId']
        url = "https://music.163.com/api/v1/user/detail/" + str(userId)
        resp = requests.get(url, headers=headers)
        user = resp.json()
        user_item = (user['userPoint']['userId'],'蜂王团队', user['profile']['nickname'],'123456', '14752191369', '1244353765@qq.com', user['profile']['avatarUrl'], user['profile']['gender'],'0', '0', timeStamp(user['userPoint']['updateTime']), timeStamp(user['profile']['createTime']), '00000')
        val.append(user_item)
    print(len(val))
    with open('./语法基础/res/json/val111.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = 'INSERT INTO user(user_id, user_name, nick_name, password, phone, email, avatar, gender, cloud_coin, delete_flag, update_time, create_time, salt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql,val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
        
def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

if __name__ == '__main__':
    data = get_song_list_comment()
    # print(timeStamp(-2209017600000))