
"""
将字符串（）中的大写字母改变
#########
while True:
    try:
        a = input()
        res = []
        for i in (a):
            if i == '(' or i == ")":
                
                 res.append(a.index(i))
        b = a[res[0]+1:res[1]]
        res1 = ''
        for i in b :
            if i.isupper():
                res1+=i.lower()
            else:
                res1+=i
                
        res2=a[:res[0]+1]+res1+a[res[1]:]
        
        print(res2)
    except:
        break
"""