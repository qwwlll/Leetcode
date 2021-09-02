"""
#不用库 取立方根（二分法）
def cube(num):
   
    if num == 0:
        return 0
    if num > 0:
        sig = 1
    else:
        sig = -1
    num = abs(num)

    if num > 1:
        start = 0
        end = num
    else:
        start = num
        end = 1
    mid = (end + start) / 2
    while abs(mid ** 3 - num) > 0.001:
        if mid ** 3 > num:
            end = mid
        else:
            start = mid
        mid = (end + start) / 2
    return (round(sig * mid, 1))
  
while True:
    try:
        num = float(input())
        print(cube(num))
    except:
        break
"""
"""


x(n+1) = x(n) - f(xn)/f'(xn)


牛顿渐进
n= float(input())
x=1
while abs(x**3-n)>0.001:
    x=x-(x**3-n)/(3*x**2)
print(round(x,1))




n= float(input())
x=1
while abs(x**2-n)>0.001:
    x=x-(x**2-n)/(2*x)
print(round(x,1))
"""


"""
#不用库取平方根

def squ():
    a = float(input("insert number to take square: "))
    if a < 0:
        a = abs(a)
    start = 0
    end = a
    mid = (start + end) /2
    if a > 0 and a < 1:
        start = 0
        end = 1
        mid = (start + end)/2
    if a >=0:
        while abs(mid ** 2 - a) > 0.001:
            if a > 1:
                if mid ** 2 > a:
                    end = mid
                else:
                    start = mid 
                mid = (start + end )/2
            elif a == 0 or a == 1:
                mid = mid
            else:
                if mid ** 2 > a:
                    
                    end = mid
                else:
                    start = mid 
                mid = (start + end )/2
                
    return(round(mid, 1))
                    
while True:
    try:
        print(squ())
    except:
        break
"""




"""
分解质因数
import math
def whether_prime_number(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        continue
    return True
            
while True:
    try:
        res = []
        n = int(input())
        if whether_prime_number(n):
            res.append(n)
        else:
            for i in range(2,int(n/2)+1):
                while n % i == 0:
                    res.append(i)
                    n = n // i
                if whether_prime_number(n):
                    res.append(n)
                    break
        for i in sorted(res):
            print(i, end=' ')
    except:
        break
"""


"""
合并表格记录
Dictionary
while True:
    try:
        dic = {}
        a = int(input())
        for i in range(a):
            key,val = map(int,input().split())
            if key not in dic:
                dic[key] = val
            else :
                dic[key] = dic[key]+val
        dics = sorted(dic)
        for i in dics:
            print(i, dic[i])
    except:
        break
"""


"""
提取不重复的整数

while True:
    try:
        res = []
        n = input()
        x = n[::-1]
        for i in x:
            if i not in res:
                res.append(i) 
        m = 0
        k = len(res) -1
        for i in res:
            s = (int(i))
            m = s *(10 ** k) + m
            k = k -1 
        print(m)
    except:
        break
"""

"""
字符个数统计

while 1:
    try:
        a = input()
        res =[]
        for i in a:
            if i not in res:
                res.append(i)
        print(len(res))
                
        
    except:
        break
"""



"""
字符串排序


while 1:
    try:
        res = []
        a = int(input())
        for i in range (a):
            res.append(input())
        resd = sorted((res))
        for i in resd:
            print(i)
    except:
        break
"""


"""
简单密码

while True:
    try:
        res = []
        a = input()
        for i in (a):
            if i.isupper() and i != 'Z':
                res.append( chr(ord(i.lower()) + 1))
            elif i == 'Z':
                res.append('a')
            elif i.isdigit():
                res.append(i)
            elif i in 'wxyz':
                res.append('9')
            elif i in 'tuv':
                res.append('8')
            elif i in 'pqrs':
                res.append('7')
            elif i in 'mno':
                res.append('6')
            elif i in 'jkl':
                res.append('5')
            elif i in 'ghi':
                res.append('4')
            elif i in 'def':
                res.append('3')
            elif i in 'abc':
                res.append('2')
        print(''.join(res))
    except:
        break
"""


"""

Ascii 数值排序
Ihave1nose2hands10fingers -> 0112Iaadeeefghhinnnorsssv
while True:
    try:
        n = sorted(input())
        print("".join(n))
        #print(n)
    except:
        break
"""




"""
找规律 ---- 蛇形矩阵

while True:
    try:
        N=int(input())
        res=[]
        for i in range(N):
            if i==0:
                res=[(e+2)*(e+1)//2 for e in range(N)]
            else:
                res=[e-1 for e in res[1:]]
            print(' '.join(map(str,res)))
    except:
        break
"""



"""
字符串加密
大小写混用
while True:
    try:
        word = input().upper()
        s = input()
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 字母表
        n_word = ''  # 融入加密词后的新字母表
        res = ''
        for i in word:
            if i not in n_word:  # 加密单词剔除重复字母
                n_word += i
        for i in alpha:
            if i not in n_word and len(n_word) <= 26:  # 用字母表剔除已有字母后补齐为26个新字母表n_word
                n_word += i
        for i in s:
            if i in alpha:  # 说明i是大写字母，因为alpha字母表默认值是大写字母
                res += n_word[alpha.index(i)]  # 索引值相同，根据字母表索引值在新字母表中取值后追加给返回结果
            else:  # i为小写字母
                res += n_word[alpha.index(i.upper())].lower()  # 将小写字母转换为大写字母取索引值后，追加返回结果之前将字母还原为小写字母
        print(res)
    except:
        break
"""



"""
求小球落地5次后所经历的路程和第5次反弹的高度



while True:
    try:
        a = int(input())
        long = a
        for i in range(1,5):
            long += 2 * a * (1/2 ** i)
        high = 1/2 ** 5 * a
        print(long)
        print("%.5f" % high)
    except:
        break
"""


"""
统计字符
while 1:
    try:
        a = list(input())
        alpha = []
        kongge = []
        num = []
        other = []
        for i in a :
            if i.isalpha():
                alpha.append(i)
            elif i.isdecimal():
                num.append(i)
            elif i == ' ':
                kongge.append(i)
            else:
                other.append(i)
        print(len(alpha))
        print(len(kongge))
        print(len(num))
        print(len(other))
    except:
        break
"""


"""

名字的漂亮度

while True:                                 #处理多组输入
    try:
        n = int(input().strip())            #接收待处理的数据个数                     
        for i in range(n):                  #接收每个待处理的字符串
            s = input().strip().lower()     
            if not s.isalpha():break        #输入不是字母为非法输入
            l = []                          
            res = 0
            for i in list(set(s)):          #记录字母出现次数
                l.append(s.count(i))
            l = sorted(l,reverse=True)      #将字母出现次数从大到小排序
            for i in range(len(l)):         #计算最大漂亮度
                res += l[i]*(26-i)            
            print(res)
    except:
        break
"""






"""

截取字符串
while True:
    try:
        a = (input())
        b = int(input())
        print(a[:b])
    except:
        break
"""



"""
从单向链表中删除指定值的节点
while True:
    try:
        ss = input().strip().split()
        n = int(ss[0])
        L = []
        L.append(ss[1])
        c_list = ss[2:-1]
        #按规则构造列表
        for i in range(n-1):
            v = c_list[2*i]
            f = c_list[2*i + 1]
#             print(v,f)
            index = L.index(f)
#             print(index)
            L.insert(index + 1, v)
#         print(L)
        L.remove(ss[-1])
#         if len(L) == 0:
#             print("0")
#         else:
        print(" ".join(L))
    except:
#         print(sys.exc_info())
        break

"""
