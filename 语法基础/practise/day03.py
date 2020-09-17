素数
num = int(input('输入一个正整数'))
a = 2
b = True
c = True
while num == 1:
    c = False
    break
while a < num:
    if num % a == 0:
        b = False
    a += 1
if b & c:
    print(num, "是素数")
else: 
    print(num, "不是素数")
