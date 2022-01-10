# import sys

# while 1:
#     try:
#         lt  = []
#         for line in sys.stdin:
#             print(line)
#     except:
#         break

def countinga (lt):
    n = len(lt)
    dic = {}
    for i in range(n):
        if lt[i][0] in dic:
            dic[lt[i][0]] += int(lt[i][1]) 
        else: 
            dic[lt[i][0]] = int(lt[i][1]) 
    count = 0
    for a, b in dic.items():
        if b >= 10:
            count += 1
    return count



lt = [["Test1","3"],["Test1","7"],["morale1","7"], ["morale3","6"], ["morale1","4"], ["hdgkshc1","5"] ]
print(countinga(lt))





import sys
def countinga (lt):
    n = len(lt)
    dic = {}
    for i in range(n):
        if lt[i][0] in dic:
            dic[lt[i][0]] += int(lt[i][1]) 
        else: 
            dic[lt[i][0]] = int(lt[i][1]) 
    count = 0
    for a, b in dic.items():
        if b >= 10:
            count += 1
    return print(count)

lt = []
for line in sys.stdin:
    res = []
    for li in line:
        res.append(li)
    lt.append(res)
countinga(lt)