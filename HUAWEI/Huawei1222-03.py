#### A-B最短的距离
from typing import List
def min_distance(a:List[List[int]]):
    m, n = len(a), len(a[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = a[0][0]
    for i in range ( m):
        for j in range( n):
            if i == 0 and j != 0:
                dp[i][j] = dp[i][j-1] + a[i][j]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i-1][j] + a[i][j]
            else:
                dp[i][j] = a[i][j] + min(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]



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
#### 加油站问题
def min_distance1(a:List[List[int]]):
    
    return 

# while 1:
#     try:

#     except:
#         break