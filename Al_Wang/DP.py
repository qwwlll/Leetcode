from typing import List,Tuple
##### Dynamic Programming:
##### leetcode: 322,121,53,300, 152, 120
#### example 1. 0-1 pack:
def packs(arr:List[int], capacity: int) -> int:
    n = len(arr)
    dp = [[-1]*(capacity+1)]*n
    #init
    dp[0][0] = 1
    if arr[0] <= capacity:
        dp[0][arr[0]] = 1
    
    for i in range(1, n):
        for cur_weight in range(capacity + 1 ):
            if dp[i-1][cur_weight] != -1:
                dp[i][cur_weight] = dp[i-1][cur_weight]
                if cur_weight + arr[i] <= capacity:
                    dp[i][cur_weight + arr[i]]=  1
    for j in range(capacity,0,-1):
        if dp[-1][j] == 1:
            return j




def packs_with_values(arr:List[Tuple[int, int]],capacity: int) ->int:
    n = len(arr)
    dp = [[-1]*(capacity+1)]*n
    #init
    dp[0][0] = 1
    if arr[0][0] <= capacity:
        dp[0][arr[0][0]] = arr[0][1]

    for i in range(1,n):
        for cur_weight in range(capacity + 1):
            if dp[i-1][cur_weight] != -1:
                dp[i][cur_weight] = dp[i-1][cur_weight]
                if cur_weight + arr[i][0] <= capacity:
                    dp[i][cur_weight + arr[i][0]] = max(dp[i][cur_weight + arr[i][0]], dp[i-1][cur_weight]+ arr[i][1])
    return max(dp[-1])






items_info = [2, 2, 4, 6, 3]
capacity = 9
print(packs(items_info, capacity))




items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
capacity = 8
print(packs_with_values(items_info, capacity))



### example 2. 杨辉三角最小路径
def minRounte(nums: List[int]) -> int:
    n = len(nums)
    while n > 0 :
        dp = [[0] * n] * n
        #init
        dp[0][0] = nums[0][0]
        for i in range(1,n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i-1][0] + nums[i][0]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + nums[i][j]
                else:
                    dp[i][j] = min((dp[i-1][j-1] + nums[i][j]),(dp[i-1][0] + nums[i][0]))
        return min(dp[n-1])

nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
print(minRounte(nums))


#### example 3. 长方形中的最小路径
class Solution:
    def minPathSum(self , matrix: List[List[int]]) -> int:
        # write code here
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*m]*n
        #init
        dp[0][0] = matrix[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j!= 0:
                    dp[i][j] = matrix[i][j] + dp[i][j-1]
                elif i != 0 and j== 0:
                    dp[i][j] = matrix[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j] , dp[i][j-1])
        return dp[-1][-1]