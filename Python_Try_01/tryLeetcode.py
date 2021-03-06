# from typing import List
# ### leetcode26: 删除有序数组中的重复项
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         index = 1
#         n = len(nums)
#         for i in range(n-1):
#             if nums[i] != nums[i+1]:
#                 nums[index] = nums[i+1]
#                 index += 1
#         return index

# ###jzII 032:有效的变位词
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if s ==t :
#             return False
#         def countingl(s:str):
#             dic = {}
#             for i in s:
#                 dic[i] = s.count(i)
#             return dic
#         n =countingl(s)
#         m =countingl(t)
#         return n == m

# ### leetcode 160 链表相交
# #  Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if headA == None or headB == None:
#             return 
#         a = headA
#         b = headB
#         while a != b :
#             if a:
#                 a = a.next
#             else:
#                 a =headB
#             if b:
#                 b = b.next
#             else:
#                 b = headA
#         return a     

# #### leetcode 62.  不同路径(dp)

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[0]*n]*m
#         if m == 1 and n == 1:
#             return 1
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 or j == 0:
#                     dp[i][j] = 1
#                 else:
#                     dp[i][j] = dp[i-1][j] + dp[i][j-1]
#         return dp[-1][-1]




# #### leetcode 58. 最后一个单词的长度
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])




# #### leetcode 53. 最大子序和 (dp)
# class Solution:
#     def maxSumArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0]*n
#         #init
#         dp[0] = nums[0]
#         for i in range(1, n):
#             dp[i] = max(dp[i-1]+nums[i],nums[i])
#         return max(dp)



# #### leetcode 152. 乘积最大子数组
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0
#         imax, imin, res = nums[0],nums[0],nums[0]
#         for i in range(1,n):
#             imax, imin = max(nums[i]* imax, nums[i]* imin, nums[i]),min(nums[i]* imax, nums[i]* imin, nums[i])
#             res = max(res, imax)
#         return res


# ####leetcode 66. 加一
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)
#         for i in range(n-1, -1, -1):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 return digits

#         return [1] + [0] * n

# class Solution:
#     def addBinary(self, a, b):
#         res = ""
#         carry = 0
#         i = len(a) - 1
#         j = len(b) - 1
#         while i >= 0 or j >= 0 or carry != 0:
#             digitA = int(a[i]) if i >= 0 else 0
#             digitB = int(b[j]) if j >= 0 else 0
#             sum = digitA + digitB + carry
#             carry = 1 if sum >= 2 else 0
#             sum = sum - 2 if sum >= 2 else sum
#             res += str(sum)
#             i -= 1
#             j -= 1
#         return res[::-1]        

# #### leetcode 121. 买卖股票的最佳时机
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 0:
#             return 0
#         dp = [0]*n
#         minP = prices[0]
#         for i in range(1,n):
#             minP = min(prices[i],minP)
#             dp[i] = max(dp[i-1], prices[i]- minP)
#         return dp[-1]

# ### leetcode 122. 买卖股票的最佳时机 II (可多次操作)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         if n == 0:
#             return 0
#         if n == 1:
#             return 0
#         if n > 1:
#             ### dp[i][0] 前i天手上不持股票最大收益
#             ### dp[i][1] 前i天手上持股票最大收益
#             dp = [[0]*n for _ in range(n)]
#             dp[0][0] = 0
#             dp[0][1] = -prices[0]
#             for i in range(1,n):
#                 dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
#                 dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
#             return dp[n-1][0]


# ####leetcode 64. 最小路径和
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m, n  = len(grid), len(grid[0])
#         if m == 1 and n == 1:
#             return grid[0][0]
#         dp = [[0]*n for _ in range(m )]
#         dp[0][0] = grid[0][0]
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j != 0:
#                     dp[i][j] = dp[i][j-1]+ grid[i][j]
#                 elif i!=0 and j == 0:
#                     dp[i][j] = dp[i-1][j] + grid[i][j]
#                 else:
#                     dp[i][j] = min(dp[i][j-1] +grid[i][j],dp[i-1][j]+grid[i][j] )
#         return dp[-1][-1]
for i in range (5):
    print(i)
