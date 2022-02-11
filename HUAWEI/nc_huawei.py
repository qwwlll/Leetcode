#### HJ13 句子逆序
a = input().split()
res = ""
for i in range(len(a)):
    res += a[len(a)-i-1]
    res += " "
print(res)


####HJ17 坐标移动
moves = input().split(";")
front,back = 0, 0
for move in moves:
    count = 0
    for i in range(len(move)):
        if move[i].isalpha():
            count += 1
        if not move[1:]:
            break
    if count == 1:
        if move[0] == "A":
            front -= int(move[1:])
        elif move[0] == "D":
            front += int(move[1:])
        elif move[0] == "W":
            back += int(move[1:])
        elif move[0] == "S":
            back -= int(move[1:])
res = str(front) + ","+str(back)
print(res)

#### HJ20 密码验证合格程序
while 1 :
    try:
        line = input()
        flag = True
        a,b,c,d = 0,0,0,0
        for x in line:
            if x.isdigit():
                a = 1
            elif x.islower():
                b = 1
            elif x.isupper():
                c = 1
            else:
                d = 1
        for j in range(len(line) - 3):
            if line.count(line[j:j+3])>1:
                flag = False
        if len(line) > 8 and (a + b + c + d)>= 3 and flag:
            print("OK")
        else:
            print("NG")
    except:
        break


#### HJ27  查找兄弟单词


while 1:
    try:
        a = input().split()
        target_num,rank_num,target  = int(a[0]),int(a[-1]),a[-2]
        words = a[1:-2]
        bro = []
        count = 0
        for word in words:
            if sorted(target)== sorted(word) and target != word:
                count += 1
                bro.append(word)
        print(count)
        print(sorted(bro)[rank_num - 1])

    except:
        
        break

#### HJ31 单词倒排
while 1:
    try:
        
        a = input()
        b = []
        for i in a:
            if not i.isalpha():
                a = a.replace(i," ")
        for j in a.split():
            b.append(j)
        print(" ".join(b[::-1]))
    except:
        break



#### HJ35 蛇型矩阵

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


#### 