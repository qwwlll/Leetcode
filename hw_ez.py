"""
while True:
    try:
        a = input()
        b = str(a)
        print(b[::-1])
    except:
        break

"""
#反转字符串
    #while True:
        #try:
        #a = input()
        #print(a[::-1])
        
    #except:
    #    break


"""
取最大公约数
def gcd (a, b):
    if b == 0 :
        return a 
    else:
        return gcd(b , a%b)
    
    
while True:
    try:
        a , b = map(int, input().split())
        print ( a * b // gcd(a, b)) 
        ## a x b / 两个数的最大公约数  == 最小公倍数
    except:
        break

"""

"""
字符串倒叙
while True:
    try:
        a = input()
        print(a[::-1])
    except:
        break
"""
"""
等差数列 求和
while True:
    try:
        a1, d, n = 2, 3, int(input())
        #Sn=n*a1+n(n-1)d/2
        res = n * a1 + n * (n - 1) * d //2
        print(res)
    except:
        break
"""
"""
等比数列 求和
while True:
    try:
        a1, q, n = 2, 3, int(input())
        #Sn=a1(1-q^n)/(1-q)
        res = a1 * (1 - q.pow(n))/(1 - q)
        print(res)
    except:
        break
"""
"""
计负均正
while True:
    try:
        a,nums,pos,neg=int(input()),map(int,input().split()),[],0
        for num in nums:
            if num>0:
                pos.append(num)
            elif num<0:
                neg+=1
        print(str(neg)+" 0" if not pos else str(neg)+" "+"{0:.1f}".format(sum(pos)/len(pos)))

    except:
        break
"""
"""
dp 动态规划格子里的最短路经

def uniquePath(m, n):

    res=[[1]*n for i in range(m)]

    for i in range (1, m):
        for j in range (1,n):
            res[i][j] = res[i-1][j]+ res[i][j-1]
    return res[m-1][n-1]
    
while True:
    try:
        print(uniquePath(* map(lambda c:int(c)+1,input().split())))
    except:
        break
""" 




"""
二进制里有多少个连续的1

while True:
    try:
        a = input()
        b = bin(int(a))[2:] #变成bin 去掉0b
        c = str(b).split('0')#换到str 用0 分开
        d = 0
        for i in c:
            d = max(d,len(i)) #挑选最大长度
        print (d)
    except:
        break
    
"""
"""
import re
十六进制 用数字分割字母
while True:
    try:
        a = hex(int(input()))[2:]
        b = str(a)
        c = re.split('(\D+)', b)
        print (c)

    except:
        break
"""




"""
最长回文字符串
def def_huiwen(pswd):
    for i in range(len(pswd),0,-1):
        for j in range (0,len(pswd)-i+1):
            if pswd[j:j+i] == pswd[j:j+i][::-1]:
                return i
while True:
    try:
        a = input()
        print(def_huiwen(a))
    except:
        break
            
"""
"""


统计字符串中的大写字母
while True:
    try:
        a = input()
        num_up = 0
        for i in a:
            if i.isupper():
                num_up += 1
            else:
                pass
        print(num_up)
         
    except:
        break
            
"""

"""
检查坐标

while True:
    try:
        m,n = map(int,input().split())
        if m > 9 or n > 9:
            print(-1)
        else:
            print(0)
        x1,y1,x2,y2 = map(int,input().split())
        if x1 >= m or x2 >= m or y1 >= n or y2 >= n:
            print(-1)
        else:
            print(0)
        x = int(input())
        y = int(input())
        if x >= m or x < 0 or m + 1 > 9:
            print(-1)
        else:
            print(0)
        if y >= n or y<0 or n + 1 > 9:
            print(-1)
        else:
            print(0)
        x,y = map(int,input().split())
        if x >= m or y >= n:
            print(-1)
        else:
            print(0)
    except:
        break
"""
"""

尼科彻斯定理

验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
while True:
    try:
        tar = int(input())
        target = tar * tar * tar
        #first state tar*tar -(tar-1)
        a = tar*tar -(tar-1)
        res = str(a)
        for i in range (1, tar):
            a = a + 2
            res = res + '+'+ str(a)
            
        print (res)
 
    except:
        break
"""


"""
最长公共字符串

while True:
    try:
        a = input()
        b = input()
        len_com = 0
        if len(a)>len(b):
            a , b = b, a 
        for i in range(len(a)):
            if a[i-len_com:i+1]in b:
                len_com += 1
        print(len_com)
    except:
        break
"""
"""


参数解析
while True:
    try:
        s=input()
        temp,res=[],[]
        for i,x in enumerate(s):
            if x=='"':
                temp.append(i)
        while temp:
            if s[temp[0]:temp[1]].find(' ')!=-1:
                a=s[temp[0]:temp[1]].replace(' ','++++')
                s=s[:temp[0]]+a+s[temp[1]+1:]
            temp.pop(0)
            temp.pop(0)
        res=s.split()
        for j in range(len(res)):
            res[j]=res[j].replace('++++',' ')
            if res[j].find('"')!=-1:
                res[j]=res[j].replace('"','')
        print(len(res))
        for k in res:
            print(k)
    except:
        break
"""

"""
一年中的第几天
while True:
    try:
        year, month, day = map(int,input().split())
        d = 0
        check = [31,28,31,30,31,30,31,31,30,31,30,31]
        d = sum(check[:month-1])
        if  month > 2 and (year%4 == 0 and year%100 != 0 or year%400 == 0):
            d = d +1
        print(d+day)
            
    except:
        break
"""



"""
百钱买百鸡
while True:
    try:
        a  = int(input())
        for i in range (20):
            for j in range (30):
                for k in range (100):
                    if 5 * i + 3 * j + k/3 == 100 and (i+j+k == 100):
                        
                        print(i,j,k)
        
        
        
    except:
        break
"""



"""
算二进制里有多少个1
while True:
    try:
        a = bin(int(input())).count('1')
       
        print(a)
        
    except:
        break



"""

"""
四则运算
while True:
    try:
        a = input()
        a = a.replace("{", "(")
        a = a.replace("}", ")")
        a = a.replace("[", "(")
        a = a.replace("]", ")")
        print(int(eval(a))) 
    except:
        break
"""
