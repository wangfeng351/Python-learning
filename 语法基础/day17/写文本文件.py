def main():
    str = "机会是需要等待的，可能力却是自己努力的，fighting for yourself！！！"
    # w写入，如果文件存在，则清空内容后写入，不存在则创建
    try:
        f = open("./语法基础/res/test.txt", "w", encoding="utf-8")
        print(f.write(str))
        f.close

        # a写入，文件存在，则在文件内容后追加写入，不存在则创建
        f = open("./语法基础/res/test.txt", "a", encoding="utf-8")
        print(f.write(str))
        f.close()

        # with关键字系统会自动关闭文件和处理异常
        with open("./语法基础/res/test.txt", "w") as f:
            f.write(str)
        
    except IOError as e:
        print(e)
    print("写入完毕")

if __name__=='__main__':
    main()