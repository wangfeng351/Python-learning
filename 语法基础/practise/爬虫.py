"""
爬取简书大学堂精选好课练习
"""
import requests 
import json
import pymysql
import time
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 爬取数据
def getData():
    classes_data = []
    for page in range(1, 20):
        url = "https://www.jianshu.com/asimov/collections/slug/e048f1a72e3d/public_notes?page=" + \
             str(page)+"&count=10&order_by=commented_at"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        classes_data += response.json()
    try:
        with open('./语法基础/res/json/简书.json', 'w', encoding='utf-8') as fs:
            json.dump(classes_data, fs)
    except IOError as e:
        print(e)
    print("爬取数据成功")
    return classes_data

# 数据库插入
def data_insert(classes_data):
    db = pymysql.connect("rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "db_spring")
    cursor = db.cursor()
    val = []
    for dic in classes_data:
        it = dic['object']['data']
        item = (it['id'],it['title'],it['list_image_url'],
                it['public_abbr'],it['user']['nickname'],
                it['public_comments_count'],it['total_rewards_count'],
                it['likes_count'],it['views_count'])
        val.append(item)
    sql = "INSERT INTO t_jian_article(id,title,img_url,content,author,comments,rewards_count,likes_count,views_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try: 
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    print("数据插入成功")

# 从数据库查询数据
def get_data():
    db = pymysql.connect("rm-m5ee476bu350735gjeo.mysql.rds.aliyuncs.com", "root", "XuNiit_#", "db_spring")
    cursor = db.cursor()
    sql = "SELECT * FROM t_jian_article ORDER BY views_count DESC LIMIT 10 " ;
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        db.rollback()
    finally:
        db.close()  
    return results
    print("数据查询成功")

# 展示数据
def show_data(clazz_data):
    # 造x轴数据
    name_data = []
    # 造y轴数据
    views_data = []
    # 对传过来的参数循环，给x,y轴数组添加数据
    for item in clazz_data:
        name_data.append(item[1][0:3])
        views_data.append(item[8])
    bar1 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add_xaxis(name_data)
        .add_yaxis(' ', views_data)
        .set_global_opts(title_opts=opts.TitleOpts(title='热力榜文章', subtitle='文章来自简书'))
    )
    bar1.render(path="热力榜文章.html")
    print("绘图成功")

if __name__ == "__main__":
    data_insert(getData())
    list = get_data()
    show_data(list)
  
