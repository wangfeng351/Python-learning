import requests
from lxml import etree
import json
import pymysql
import time
import random
import uuid
from faker import Faker
fake = Faker(locale='zh_CN')

headers = {
    'cookie': '_ntes_nnid=afc0b8c00fad7edac3529e13eb239079,1571915383131; _ntes_nuid=afc0b8c00fad7edac3529e13eb239079; __remember_me=true; WM_TID=YqM7BhU3VFBAVQBERUJ%2BUg%2Bozg%2BbhufE; MUSICIAN_COMPANY_LAST_ENTRY=316304066_musician; ntes_kaola_ad=1; WM_NI=8ccty8AYLgtKA5VvZoxNL9GiPnJnWaoCsUHIMlqs8rINtCNokTXpcogr2spFzUHcgOc0j82HgOTFATWvMUT%2FPegwi3Bd67p5xn00l2CrAO27Xrff%2B%2B76zJqs4cVDAtKJa1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed4fb7fb18a97d1e56bb19a8eb6c55b928b9baef15ead9afc82bb5ffcea96a9dc2af0fea7c3b92afcbdad95fc3483878488f74183eb9a97d965bc9284dac66394b2868fd66bad9dbdb6cb438fb4bf94bb7a8b92bca4cd65a98c9891e265a5aefe94f34eba8b8884e645a1f0a6d9b144a5919ca7c46095aa83b6d72594bba998ec3982bcfad8f33fbcb200d1ef3a81ae8fb0b13d9caeaa87aa21f5eab6abf479f8bd9aa5c4808996afd2d837e2a3; _iuqxldmzr_=33; JSESSIONID-WYYY=4vZFNPbaFcTomgzjs%2BZw3IXEtsZJU1zV9nXX2mJSys06YtWQNYC4EbHFjEO4Zhr05y5YpP087zMg7CJ0UQ%5CUOSF8z60xv6IGzsRzDy1NiBo8Xj157zfPUNIxX54jw1Vk685eMCXWDg6Tdu0u7NPFI45uCPf3PZTt2U60AAZZOqE6aHU%2B%3A1587102528986; playerid=55462361; MUSIC_U=ce1299bbfe2c8ced31eb76bf7c9a11bfcadf7a4d0478731a0d3bc96c04292f92f6dbb9e080384a87c20b862285ca8ec87955a739ab43dce1; __csrf=cd7bb5e8c6e740481ae96c662e06a751',
    'origin': 'https://music.163.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
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
    }
    response = requests.post(url, data=data, headers=headers)
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
    response = requests.post(url, data=data, headers=headers)
    with open('./语法基础/res/json/comment.json', 'w') as fs:
        json.dump(response.json(), fs,  ensure_ascii=False)
    print(response.json())

# 歌单评论


def get_song_list_comment(song_list_id):
    for item in range(0, 1000, 100):
        url = 'http://music.163.com/api/v1/resource/comments/A_PL_0_' + \
            str(song_list_id) + '?limit=2' + '&offset=' + str(item)
        resp = requests.get(url, headers=headers)
        data = resp.json()
        insert_song_list(data)
        insert_song_list_comment(data, song_list_id)
        insert_user(data)
        insert_user_song_list(data)

# 插入歌单评论


def insert_song_list_comment(song_list_data, song_list_id):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_list_data['comments']:
        user = dic['user']
        # user_item = (user['userId'],'123', user['nickname'], user['avatarUrl'],'2000-1-1 20:00:00', '2000-1-1 20:00:00')
        comment = (str(dic['commentId']), song_list_id, str(
            user['userId']), dic['content'], dic['likedCount'], timeStamp(dic['time']), timeStamp(dic['time']))
        val.append(comment)
    with open('./语法基础/res/json/val.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = "INSERT IGNORE INTO song_comment(id, song_list_id, user_id, comment_content, like_counts, create_time, update_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

# 插入用户


def insert_user(song_list_data):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_list_data['comments']:
        userId = dic['user']['userId']
        url = "https://music.163.com/api/v1/user/detail/" + str(userId)
        resp = requests.get(url, headers=headers)
        user = resp.json()
        address = fake.province() + fake.city_name()
        email = ''
        for i in range(0, 10):
            email += str(random.randint(0, 9))
        email += '@qq.com'
        key_id = uuid.uuid1()
        user_item = (user['userPoint']['userId'], fake.name(), user['profile']['nickname'], '123456', fake.phone_number(), email, user['profile']
                     ['avatarUrl'], user['profile']['gender'], address, '0', '0', timeStamp(user['userPoint']['updateTime']), timeStamp(user['profile']['createTime']), str(key_id).replace(
            '-', ''))
        val.append(user_item)
    print(len(val))
    with open('./语法基础/res/json/val111.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = 'INSERT IGNORE INTO user(user_id, user_name, nick_name, password, phone, email, avatar, gender,address, cloud_coin, delete_flag, update_time, create_time, salt) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

# 插入用户歌单


def insert_user_song_list(song_list_data):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_list_data['comments']:
        userId = dic['user']['userId']
        url = "http://localhost:3000/user/playlist?uid=" + str(userId)
        resp = requests.get(url, headers=headers)
        user_song_list = resp.json()
        for ls in user_song_list['playlist']:
            key_id = uuid.uuid1()
            item = (str(key_id).replace('-', ''), ls['id'], ls['creator']['userId'], timeStamp(
                ls['createTime']), timeStamp(ls['updateTime']))
            val.append(item)
    print(len(val))
    with open('./语法基础/res/json/user_list.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = 'INSERT IGNORE INTO user_song_list(id, song_list_id, user_id, create_time, update_time) VALUES (%s,%s,%s,%s,%s)'
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

# 插入歌单


def insert_song_list(song_list_data):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_list_data['comments']:
        userId = dic['user']['userId']
        url = "http://localhost:3000/user/playlist?uid=" + str(userId)
        resp = requests.get(url, headers=headers)
        user_song_list = resp.json()
        for ls in user_song_list['playlist']:
            url = 'http://localhost:3000/comment/playlist?id=' + str(ls['id'])
            resp1 = requests.get(url, headers=headers)
            # insert_song_list_comment(resp1.json())
            # insert_user(resp1.json())
            # insert_user_song_list(resp1.json())
            # insert_song(ls['id'])
            try:
                comment_count = resp1.json()['total']
            except:
                comment_count = 0
            item = (ls['id'], ls['name'], ls['coverImgUrl'], ls['adType'], ls['trackCount'],
                    ls['subscribedCount'], comment_count, 1, timeStamp(ls['createTime']), timeStamp(ls['updateTime']), ls['playCount'])
            val.append(item)
    sql = "INSERT IGNORE INTO song_list(song_list_id, song_list_name, thumbnail, type, song_count, like_count, comment_count, delete_flag, update_time, create_time, play_counts) \
        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
    # sql = 'INSERT INTO song_list(song_list_id, song_list_name, thumbnail, type, song_count, like_count, comment_count, delete_flag, update_time, create_time) \
    #     VALUES (424207055, "【史诗纯音】画面感max 震撼灵魂的经典旋律", "https://p1.music.126.net/o911nBJmDFbVI-ci9zm01A==/1406275385023856.jpg", 0, 99, 803402, 2257, 1, "2016-07-18 02:33:06", "2020-01-09 22:21:41")'
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

# 插入歌曲


def insert_song(song_list_id):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    print(song_list_id)
    url = 'https://music.163.com/api/playlist/detail?id=' + str(song_list_id)
    resp = requests.get(url, headers=headers)
    tracks = resp.json()['result']['tracks']
    # 查询歌单歌曲
    insert_song_list_music(resp.json()['result'])
    id = ''
    id_list = []
    for song in tracks:
        id += str(song['id']) + ','
        id_list.append(song['id'])
    id = id[0: len(id)-1]
    # 抓取歌曲评论信息
    # get_song_comment(id_list)
    song_detail_url = 'http://localhost:3000/song/detail?ids=' + id
    resp1 = requests.get(song_detail_url, headers=headers)
    songs = resp1.json()['songs']
    # print(songs)
    val = []
    for song1 in songs:
        song_url = 'http://music.163.com/song/media/outer/url?id=' + \
            str(song1['id']) + '.mp3'
        lrc_url = 'http://localhost:3000/lyric?id=' + str(song1['id'])
        lrc_data = requests.get(lrc_url, headers=headers).json()
        # print(song1['id'])
        try:
            lrc = lrc_data['lrc']['lyric']
        except:
            lrc = " "
        item = (song1['id'], song1['name'], 0, song1['ar'][0]['name'], songTimeStamp(song1['dt']), song1['al']['picUrl'],
                song_url, lrc, 1000, 0, 0, 0, timeStamp(song1['publishTime']), timeStamp(song1['publishTime']))
        val.append(item)
    print(val)
    sql = "INSERT IGNORE INTO song(song_id, song_name, sort_id, singer, duration, thumbnail, url, lyric, comment_count, like_count, play_count, delete_flag, create_time, update_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

# 查询歌曲评论


def get_song_comment(song_id_data):
    print(song_id_data)
    for song_id in song_id_data:
        song_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + \
            str(song_id)
        resp = requests.get(song_url, headers=headers)
        total = resp.json()['total']
        print("数量", total)
        if(total > 1000):
            total = 1000
        for offset in range(0, total, 100):
            song_comment_url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_' + \
                str(song_id) + '?limit=100&offset=' + str(offset)
            # 歌曲评论内容
            comment_data = requests.get(
                song_comment_url, headers=headers).json()['comments']
            insert_song_comment(comment_data)

# 插入歌曲评论


def insert_song_comment(song_comment_data):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for dic in song_comment_data:
        user = dic['user']
        # user_item = (user['userId'],'123', user['nickname'], user['avatarUrl'],'2000-1-1 20:00:00', '2000-1-1 20:00:00')
        comment = (str(dic['commentId']), '19723756', str(user['userId']), dic['content'],
                   dic['likedCount'], timeStamp(dic['time']), timeStamp(dic['time']))
        val.append(comment)
    with open('./语法基础/res/json/song_comment.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = "INSERT IGNORE INTO song_comment(id, song_id, user_id, comment_content, like_counts, create_time, update_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


# 插入歌单歌曲
def insert_song_list_music(datas):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for data in datas['tracks']:
        try:
            ratio = data['ratio']
        except:
            ratio = ''
        item = (datas['id'], data['id'], timeStamp(
            datas['createTime']), timeStamp(datas['updateTime']), ratio)
        val.append(item)
    with open('./语法基础/res/json/song_list_music.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = "INSERT IGNORE INTO song_list_music(song_list_id, song_id, create_time, update_time, ratio) VALUES (%s,%s,%s,%s,%s)"
    # sql = "INSERT INTO user(user_id, user_nickname, avatar, update_time, create_time) VALUES(%s, %s, %s, %s, %s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()

# 所有排行榜


def get_top_list():
    url = 'http://localhost:3000/toplist/detail'
    resp = requests.get(url, headers=headers)
    list = resp.json()['list']
    for ls in list:
        print(ls['name'])


# 歌单类型
def get_type():
    url = 'http://localhost:3000/playlist/catlist'
    types = requests.get(url, headers=headers).json()['sub']
    # 插入类型
    # insert_type(types)
    get_song_list_type(types)
    return types

# 插入歌单类型


def insert_type(datas):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    ticks = time.time()
    for tag in datas:
        key_id = uuid.uuid1()
        item = (str(key_id).replace(
            '-', ''), tag['name'], tag['resourceCount'], 0, timeStamp(ticks), timeStamp(ticks), tag['type'])
        val.append(item)
    with open('./语法基础/res/json/song_type.json', 'w') as fs:
        json.dump(val, fs,  ensure_ascii=False)
    sql = "INSERT IGNORE INTO song_type(type_id, type_name, song_count, delete_flag, update_time, create_time, type) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # sql = "INSERT INTO song_type(type_id, type_name, song_count, delete_flag, update_time, create_time, type) VALUES ('ebd9f36e814711eaa0d0b4b686bbf77b', 'Bossa Nova', 1000, 0, '1970-01-19 16:53:15', '1970-01-19 16:53:15', 1)"
    try:
        cursor.executemany(sql, val)
        # cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


# 获取歌单类型关联
# 参数 所有类型集合
def get_song_list_type(datas):
    for data in datas:
        for offset in range(0, 300):
            url = 'http://localhost:3000/top/playlist?limit=100&cat=' + \
                str(data['name']) + '&offset=' + str(offset)
            song_list_data = requests.get(
                url, headers=headers).json()['playlists']
            insert_song_list_type(song_list_data, data['name'])

# 插入歌单类型
# 参数： 类型返回的歌单， 类型名


def insert_song_list_type(song_list_data, data):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    print('类型：' + str(data))
    cursor = db.cursor()
    val = []
    ticks = time.time()
    for song_list in song_list_data:
        get_song_list_comment(song_list['id'])
    #     key_id = uuid.uuid1()
    #     item = (str(key_id).replace('-', ''), song_list['id'], timeStamp(song_list['createTime']), timeStamp(song_list['updateTime']), data)
    #     # 插入歌单点赞
    #     # get_song_like(song_list['id'])
    #     val.append(item)
    # print(val)
    # sql = "INSERT IGNORE INTO type_song_list(id, song_list_id, create_time, update_time, type_name) VALUES (%s, %s, %s, %s, %s)"
    # # sql = "INSERT INTO song_type(type_id, type_name, song_count, delete_flag, update_time, create_time, type) VALUES ('ebd9f36e814711eaa0d0b4b686bbf77b', 'Bossa Nova', 1000, 0, '1970-01-19 16:53:15', '1970-01-19 16:53:15', 1)"
    # try:
    #     cursor.executemany(sql, val)
    #     # cursor.execute(sql)
    #     db.commit()
    # except:
    #     db.rollback()
    # finally:
    #     db.close()

# 获取歌单的用户收藏信息


def get_song_like(song_list_id):
    for offset in range(0, 1000, 100):
        url = 'http://localhost:3000/playlist/subscribers?id=' + \
            str(song_list_id) + '&limit=100&offset=' + str(offset)
        resp = requests.get(url, headers=headers).json()['subscribers']
        insert_song_like(resp, song_list_id)

# 插入歌单的用户收藏关联表信息


def insert_song_like(datas, song_list_id):
    db = pymysql.connect(
        "rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "cloud_music")
    cursor = db.cursor()
    val = []
    for data in datas:
        key_id = uuid.uuid1()
        item = (str(key_id).replace(
            '-', ''), data['userId'], song_list_id, '2020-01-01 02:11:11', '2020-01-01 02:11:11')
        val.append(item)
    print(val)
    sql = "INSERT IGNORE INTO song_like(like_id, user_id, song_list_id, create_time, update_time) VALUES (%s, %s, %s, %s, %s)"
    # sql = "INSERT INTO song_type(type_id, type_name, song_count, delete_flag, update_time, create_time, type) VALUES ('ebd9f36e814711eaa0d0b4b686bbf77b', 'Bossa Nova', 1000, 0, '1970-01-19 16:53:15', '1970-01-19 16:53:15', 1)"
    try:
        cursor.executemany(sql, val)
        # cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
# def get_song_comment(id, limit):
#     url = 'http://localhost:3000/comment/music?id=' + str(id) + '&limit=' + str(limit)
#     resp = requests.get(url, headers=headers)
#     return resp.json()


def timeStamp(timeNum):
    timeStamp = float(timeNum/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

# 歌曲时间转换s


def songTimeStamp(time):
    seconds = int(time/1000 % 60)
    minutes = int(time/1000/60)
    if(seconds < 10):
        seconds = '0' + ":" + str(seconds)
    if(minutes <= 9):
        minutes = '0' + str(minutes)
    return str(minutes) + ":" + str(seconds)


if __name__ == '__main__':
    # insert_song_list()
    # insert_song(19723756)
    # list = [1436709403]
    # get_song_comment(list)

    # data = get_song_list_comment(4880937603)
    # 获取歌曲
    # list = [958226333, 4958223888, 4970440143, 4880937603,947937494]
    # for ls in list:
    #     insert_song(ls)
    # print(songTimeStamp(221750))
    # 歌曲歌单关联
    # url = 'https://music.163.com/api/playlist/detail?id=19723756'
    # resp = requests.get(url, headers=headers)
    # data = resp.json()['result']
    # insert_song_list_music(data)
    # get_top_list()
    get_type()
    
    # get_song_like(3136952023)
