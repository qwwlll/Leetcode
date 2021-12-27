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


a = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
print(min_distance(a))



#### 加油站问题
def min_distance1(a:List[List[int]]):
    
    return 

# while 1:
#     try:

#     except:
#         break