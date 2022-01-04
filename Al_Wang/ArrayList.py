from typing import List
###leetcode 15 sum of the three numbers
### sort 加双指针
class Solution:
    def threeSum(self , num: List[int]) -> List[List[int]]:
        num.sort()
        n = len(num)
        res = []
        if n < 3:
            return []
        for a in range(n-2):
            if a > 0 and num[a] == num[a-1]: ## 去重
                continue
            target = 0 - num[a] ### num1 + num2 + num3 ==0 的问题转化成 num2 + num3 = - num1
            c = n - 1 ## 第二指针在尾部
            for b in range (a+1, n-1 ):
                if b > a + 1 and num[b] == num[b-1]: ## 去重
                    continue
                while b < c and num[b] + num[c] > target:
                    c = c - 1 ## 第二指针往前移动
                if b == c :
                    break
                if num[c] + num[b] == target:
                    res.append([num[a], num[b], num[c]])
        return res

###leetcode 169  MajorityNumber
### 暴力解法 （大数量集时超时） O(n^2)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        count_lt = []
        count = 0
        for i in range(n):
            for j in range (n):
                if nums[i] == nums[j]:
                    count = count + 1
            count_lt.append(count)
            count = 0
        return nums[count_lt.index(max(count_lt))]

###other way: O(1)
##多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。排序的时候，中间数一定是众数
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

###leetcode 41 missing postive number
### hash table used.





####leetcode 128 最长连续序列
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longup = 0
        for n in num:
            if n - 1 not in num:
                current_num = n
                current_steak = 1
                while current_num + 1 in num:
                    current_steak += 1
                    current_num += 1
                longup = max(longup, current_steak)
        return longup

        
### leetcode 347 前k个高频数
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic  = {}
        ks = []
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]]  = 1
        res = list(dic.items())
        res.sort(key = lambda x: x[1], reverse = True)
        for i in range(k):
            ks.append(res[i][0])
        return ks


#### leetcode 200. 岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_checking( grid, r, c):
            grid[r][c] = 0
            gr, gn = len(grid), len(grid[0])
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if  0 <= x < gr and 0 <= y < gn and grid[x][y] == "1":
                    dfs_checking(grid, x, y)
        
        r, c = len(grid), len(grid[0])
        if r == 0:
            return 0
        num_island = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    num_island += 1
                    dfs_checking(grid, i, j)
        return num_island

##### leetcode 162. 寻找峰值

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        return nums.index(max(nums))

### 华为矩阵 每列最大和
#输入
#3 4
#-3 3 -1 4
#-4 4 -2 5
# 5 5 -3 3
#输出
#18 

while True:
    try:

        row,col = map(int,input().split())
        if row == 0 or col == 0:
            print(0)
            break
        L = []
        for i in range(row):
            LL = list(map(int,input().split()))
            L.append(LL)
        L_max_sum = 0
        num_sum = 0
        for  pos_row in range(row):
            for pos_col in range(col):

                row_yu = row - pos_row
                col_yu = col - pos_col
                for i_row_yu in range(row_yu):
                    for i_col_yu in range(col_yu):
                        num_sum = 0
                        for row_num in range(i_row_yu+1):
                            for col_num in range(i_col_yu+1):
                                num_sum += L[pos_row+row_num][pos_col+col_num]
                        if L_max_sum < num_sum:
                            L_max_sum = num_sum
        print(L_max_sum)
    except:
        break


### hj91 走方格方案

while 1:
    try:
        def countGe(n , m):
            dp = [[1]*m for _ in range(n)]
            dp[0][0] = 1
            for i in range(1, n):
                for j in range(1,m):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[-1][-1]
        
        n, m = list(map(int, input().split()))
        print(countGe(n + 1 , m + 1 ))
        
        
    except:
        break

    
### hj 85 最长回文字符串
def def_huiwen(pswd):
    for i in range(len(pswd),0,-1):
        for j in range (0,len(pswd)-i+1):
            if pswd[j:j+i] == pswd[j:j+i][::-1]:
                return i
while True:
    try:
        a = input()
        print(def_huiwen(a))
    except:
        break


### leetcode 134 加油站
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total, start = 0,0
        if sum(gas) < sum(cost):
            return -1
        for i in range(n):
            total += gas[i] - cost[i]
            if total <0 :
                total = 0
                start = i + 1
        return start


### leetcode 130 被围绕的区域(dfs)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != "O":
                return 
            board[x][y] = "!"
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        
        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "!":
                    board[i][j] ="O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
            


#### leetcode 36 有效的数独
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 将二维列表按行展开成一维列表
        flatten_board = []
        for i in range(9):
            flatten_board.extend(board[i])

        # 用于判断某一行/列/块是否合法（即是否有相同的元素）
        def is_valid(m):
            counter = {}
            for el in m:
                if el != '.':
                    if el in counter:
                        return False
                    else:
                        counter[el] = 1
            return True

        # 数独有9行/9列/9块
        # 循环判断第 i 行/列/块 是否合法
        for i in range(9):
            # 数独第 i 行元素在展开后表列中的下标：[i * 9 + j for j in range(9)]
            # 数独第 i 列元素在展开后列表中的下标：[i + j * 9 for j in range(9)]
            # 数独第 i 块元素在展开后列表中的下标：[(i // 3) * 27 + (i % 3) * 3 + (j // 3) * 9 + (j % 3) for j in range(9)]
            rowi = [flatten_board[i * 9 + j] for j in range(9)]  # 数独第 i 行元素
            coli = [flatten_board[i + j * 9] for j in range(9)]  # 数独第 i 列元素
            blocki = [flatten_board[(i // 3) * 27 + (i % 3) * 3 + (j // 3) * 9 + (j % 3)] for j in range(9)]  # 数独第 i 块元素

            # 分别判断第 i 行/列/块是否合法，不合法，则数独不合法
            if is_valid(rowi) is False:
                return False
            if is_valid(coli) is False:
                return False
            if is_valid(blocki) is False:
                return False

        return True

#### leetcode 27 移除元素
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


#### leetcode 39 组合总和
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tmp = []
        ans = []
        def dfs(index):
            s = sum(tmp)
            if s == target:
                ans.append(tmp[:])
                return
            elif s > target:
                return
            for i in range(index, len(candidates)):
                tmp.append(candidates[i])
                dfs(i)
                tmp.pop()

        dfs(0)
        return ans

