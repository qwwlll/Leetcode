while True:
    try:
        a = input()
        b = str(a)
        print(b[::-1])
    except:
        break


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
""" 