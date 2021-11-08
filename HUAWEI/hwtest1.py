##字符串去重
#a = input()
#b = []
#for i in range(len(a)):
    #if a[i] not in b:
         #b.append(a[i]) 

#print("".join(b))
    
list2 = ['hello','world']
# 引号中的内容为，连接各个字符串的字符
print("".join(list2))
print(" ".join(list2))
print(".".join(list2))
# 输出：helloworld
# 输出：hello world
# 输出：hello.world

##两数相加
import sys
for line in sys.stdin:
    line.split()
print (line[0]+line[1])
