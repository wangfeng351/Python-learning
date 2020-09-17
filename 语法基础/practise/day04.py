# for循环
for i in range(5):
    i = i + 1
    while i < 6:
        if i == 5:
            a = " "
        else:
            a = ","
        print(i, end=a)
        i = i + 1
    else:
        break