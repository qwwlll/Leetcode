"""求近似值
"""
while True:
    try:
         a = float(input(""))
         b = int(a)
         c = float(a - b)
         if c < 0.5:
             shuchu = b
         else:
             shuchu = b + 1
         print(shuchu)


    except:
        break
   

"""
求输入的数字在储藏时有多少1
while True:
    try:
        a = input()
        b = bin(int(a))
        print (b.count('1'))
    except:
        break
"""