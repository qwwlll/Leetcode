from typing import List,Tuple
## Leetcode 680 验证回文字符串 Ⅱ
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(start: int, end: int, s:str):
            while start < end :
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        start, end = 0, len(s) - 1
        while start < end :
            if s[start] == s[end]:
                start += 1
                end -= 1
            
            else:return check(start, end -1 , s) or check(start + 1, end , s)
        return True


### leetcode 455 发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m, n = len(g), len(s)
        i = 0
        j = 0 
        sat = 0
        while i < m and j < n:
            while j < n and g[i] > s[j]:
                j += 1
            if j < n:
                sat += 1
            j += 1
            i += 1
        return sat

### leetcode 409. 最长回文串
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        dic = {}
        lto = []
        lte = []
        for i in s:
            dic[i] = s.count(i)
        for var in dic.values():
            if var %2 == 0:
                lto.append(var)
            else:
                lte.append(var)
        if lte == []:
            return sum(lto)
        return sum(lto) + sum(lte) - len(lte) + 1

#### leetcode 561. 数组拆分 I
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

### 605. 种花问题    
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ct = 0 
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 :
                flowerbed[i] = 1
                ct += 1
            if ct >= n: return True
        return False
     
#### 942. 增减字符串匹配  （贪心 i 选最小 d 选可选的最大的）
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start , end = 0, len(s)
        res = []
        for x in s:
            if x == "I":
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1
        return res + [start]


### leetcode 976. 三角形的最大周长
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        if n == 3:
            nums.sort(reverse = True)
            if nums[2] + nums[1] <= nums[0]:
                return 0 
            else: return sum(nums)
        if n > 3:
            nums.sort(reverse = True)
            for i in range(2, n):
                if nums[i] + nums[i-1] > nums[i-2]:
                    return nums[i-2] + nums[i-1] + nums[i]
            return 0  