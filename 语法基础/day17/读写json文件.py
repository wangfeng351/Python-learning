"""
读写json文件
@Date 2020.04.10
"""

# Json模块主页有四个比较重要的函数，分别是：
# dump - 将Python对象按照Json对象按照J格式序列号到文件中
# dumps - 将Python对象处理或JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
import json

def main():
    # 定义字典对象
    mydict = {
        'name': 'Tome',
        'age' : 21,
        'qq' : 1244353765,
        'friends' : ['Andi', 'Hobbo'],
        'cars' : [
            {'brand' : 'Aodi奥迪', 'max_speed' : 280},
            {'brand' : 'BMW宝马', 'max_speed' : 320}

        ]
    }
    try:
        # 将字典对象序列化到文件
        with open('./语法基础/res/json/Andi.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')

    try:
        # 从文件中读入, 反序列化成对象
        with open('./语法基础/res/json/Andi.json', 'r', encoding='utf-8') as fs:
            mydict = json.load(fs)
            print(mydict)

    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('保存数据完成！')

if __name__ == '__main__':
    main()