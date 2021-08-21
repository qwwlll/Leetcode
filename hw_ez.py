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
"""