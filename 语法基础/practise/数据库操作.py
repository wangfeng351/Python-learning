"""
数据库常规操作
"""

import pymysql 

def data_select():
    # 数据库连接
    db = pymysql.connect("localhost", "root", "root", "db_python")
    # 获得游标
    cursor = db.cursor()
    sql = "SELECT * FROM t_follower"
    try:
        cursor.execute(sql)
        # 执行sql
        results = cursor.fetchone()
        print('1243')
        # 打印结果
        print(results)
    except:
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    data_select()