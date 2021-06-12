#copy list
a = [ 3, 4, 5,2 ,5,6, 4,5,7,8,3]
b = a[:]
print (b)

##输出乘法表
for i in range(1, 10):
    print() 
    for j in range(1, i+1):
        print ("%d*%d=%d" % (i, j, i*j), end=" " )



##慢一秒输出
import time
 
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print ( key, value)
    time.sleep(1) # 暂停 1 秒
    ###输出当前时间
    print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


##水仙花数
##分解三位数
for n in range(100,1000):
    i = n // 100     #百
    j = n // 10 % 10 #十
    k = n % 10       #个
    if n == i**3 + j**3 + k**3: 
        print(n)


### 数str
import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():   
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))