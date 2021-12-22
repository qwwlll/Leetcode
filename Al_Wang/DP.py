from typing import List,Tuple
##### Dynamic Programming:
##### leetcode: 322,121,53,300, 152, 120
#### example 1. 0-1 pack:
def packs(arr:List[int], capacity: int) -> int:
    n = len(arr)
    dp = [[-1]*(capacity+1) for i in range(n)]
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
    dp = [[-1]*(capacity+1) for i in range(n)]
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


##### leetcode 118. 杨辉三角
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 :
            return 
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return[[1],[1,1]]
        dp = [[1]* (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range( len(dp[i])):
                if  i == j or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp


#####  leetcode 119. 杨辉三角 II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 2:
            return [1,2,1]
        dp =[[1] * (i+1) for i in range(rowIndex + 1)]
        for i in range(rowIndex+1):
            for j in range(len(dp[i])):
                if i == j or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[-1]


### example 2. 杨辉三角最小路径
def minRounte(nums: List[int]) -> int:
    n = len(nums)
    while n > 0 :
        dp = [[0] * n for _ in range (n)]
        #init
        dp[0][0] = nums[0][0]
        for i in range(1,n):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i-1][0] + nums[i][0]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + nums[i][j]
                else:
                    dp[i][j] = min((dp[i-1][j-1] + nums[i][j]),(dp[i-1][j] + nums[i][j]))
        return min(dp[n-1])

nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
print(minRounte(nums))


#### example 3. 长方形中的最小路径
class Solution:
    def minPathSum(self , matrix: List[List[int]]) -> int:
        # write code here
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*m for _ in range(n)]
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

#### example 4. 换零钱
class Solution:
    def minMoney(self , arr: List[int], aim: int) -> int:
        # write code here
        if not arr:
            return -1
        if min(arr) > aim and aim != 0:
            return -1
        if aim == 0:
            return 0
        dp = [aim+1]*(aim+1)
        dp[0] =0
        for i in range(1, aim + 1):
            for j in arr:
                if j <=i:
                    dp[i] = min(dp[i], dp[i-j]+1 )
        if dp[aim]> aim:
            return -1
        return dp[aim]

#### example 5. 最长上升子序列
#### leetcode 121. 买卖股票的最佳时机
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0]*n
        minP = prices[0]
        for i in range(1,n):
            minP = min(prices[i],minP)
            dp[i] = max(dp[i-1], prices[i]- minP)
        return dp[-1]

### leetcode 122. 买卖股票的最佳时机 II (可多次操作)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n > 1:
            ### dp[i][0] 前i天手上不持股票最大收益
            ### dp[i][1] 前i天手上持股票最大收益
            dp = [[0]*n for _ in range(n)]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1,n):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            return dp[n-1][0]

#### example 6. 最长公共字符串
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0]*(m+1) for _ in range (n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

#### leetcode 198. 打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i-2]+nums[i])
        return max(dp)



#### 牛客 0-1 背包 + value
while True:
    try:
        n, V = map(int, input().split())
        lv, lw = [], []
        for i in range(n):
            l = list(map(int, input().split()))
            lv.append(l[0])  # 物品重量列表
            lw.append(l[1])  # 物品价值列表
        dp = [0 for _ in range(V + 1)] # dp[j]表示背包容量为j时装满背包的最大价值。最终输出时，问题1的答案是整个dp的最大值，问题2的答案是dp的最后一个数，初始化时数字是0所以最后如果的不到结果也满足答案要求。
        for i in range(n):
            for j in range(V, 0, -1):  # 从后向前算，防止数据混淆
                if lv[i] <= V and(j == lv[i] or (dp[j - lv[i]] != 0 and j - lv[i] > 0)):  # 条件首先剔除无法放入背包的物品。然后如果新加入的物品可以单独放入某一个j、或者与已存在的值可以组成j的值进行计算。由于Python的特性dp需剔除负坐标j - lv[i] > 0
                    dp[j] = max(dp[j], dp[j - lv[i]] + lw[i])  # dp[j]的值只与其当前值、能与lv[i]重量组合成j重量的dp[j - lv[i]]，两个数中的较大值
        print(max(dp))
        print(dp[-1])
    except:
        break


#### 牛客 完全背包
def package():
    n, V = map(int, input().split())
    v, w = [], []
    for _ in range(n):
        vv, ww = map(int, input().split())
        v.append(vv)
        w.append(ww)
    dp = [0]+[float('-inf')]*V
    for i in range(n):
        for j in range(v[i],V+1):
            dp[j] = max(dp[j], dp[j-v[i]]+w[i])
    print(max(dp))
    if dp[-1] != float('-inf'):
        print(dp[-1])
    else:
        print(0)
package()


