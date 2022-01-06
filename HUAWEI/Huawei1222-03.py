#### A-B最短的距离
from typing import List

def min_distance(a:List[List[int]]):
    m, n = len(a), len(a[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = a[0][0]
    for i in range (m):
        for j in range(n):

            if i == 0 and j != 0:
                dp[i][j] = dp[i][j-1] + a[i][j]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i-1][j] + a[i][j]
            else:
                dp[i][j] = a[i][j] + min(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]




# def gasing( a:List[List[int]], gas_num: int):
#     if gas_num <= a[0][0]:
#         return -1
#     m, n = len(a), len(a[0])
#     dp = [[0] * n for _ in range(m)]
#     if gas_num >= a[0][0]:
#         dp[0][0] = gas_num - a[0][0]
#     else:
#         return -1
#     for i in range(1, m):
#         for j in range(1, n):
#             if  gas_num > 0 and gas_num >= a[i][j]:
#                 if a[i][j] == -1:
#                     gas_num = 100
#                 if i == 0 and j != 0:
#                     dp[i][j] = dp[i][j-1] - a[i][j]
#                     gas_num = dp[i][j] 
#                 elif i != 0 and  j == 0:
#                     dp[i][j] = dp[i-1][j]- a[i][j]
#                     gas_num = dp[i][j] 
#                 else:
#                     dp[i][j] =  max(dp[i-1][j],dp[i][j-1]) - a[i][j]
#                     gas_num = dp[i][j]
#             elif gas_num <= 0:
#                 return -1
#     return dp[-1][-1]

list = [[10, 20], [30, 40]]
gas_num = 100
list1 = [[10, 30, 30, 20],[30,30,-1,10],[10,20,20,40],[10,-1,30,40]]
# print(gasing(list, gas_num))
print(min_distance(list1))


# import sys
# def min_distance(a:List[List[int]]):
#     m, n = len(a), len(a[0])
#     dp = [[0] * n for _ in range(m)]
#     dp[0][0] = a[0][0]
#     for i in range ( m):
#         for j in range( n):
#             if i == 0 and j != 0:
#                 dp[i][j] = dp[i][j-1] + a[i][j]
#             elif j == 0 and i != 0:
#                 dp[i][j] = dp[i-1][j] + a[i][j]
#             else:
#                 dp[i][j] = a[i][j] + min(dp[i-1][j],dp[i][j-1])
#     return print(dp[-1][-1])

# while 1:
#     try:
#         list = []  
#         for line in sys.stdin:      
#             res =[]
#             for li in line.split(","):
#                 res.append(int(li))
#             list.append(res) 
#         min_distance(list)
#     except:
#         break



# 10,30,30,20
# 20,30,30,30
# 30,20,20,10
# 30,40,50,30
# 10,20
# 30,40
