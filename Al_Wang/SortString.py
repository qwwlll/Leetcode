from typing import Counter, List
### 给string 进行不同需求的排序
def sortingStr(n: List[str]) -> List[str]:
### 将list n 先以长度后以字符序排序

#    n.sort(key= lambda i :(len(i), i))

### 将list n 先以字符序排序后以长度
#    n.sort(key = lambda i:(i, len(i))) ### 先后顺序matters！

### 先将list n 以 a 的重复次数排序 后以长度后以字符序排序
    dic = {}
    def counting(x):
        return x.count('a')

###    result = sorted(dic.items(), key= lambda x: x[1],reverse= True)
### 多条件sort
    res = sorted(n, key = lambda i: (counting(i),len(i),i),reverse= True)
    return res
    



n = ['asdas', 'asfw', 'efa', 'hfeafa', 'ddefaf','abc','ac','aacs','abbcs']
print(sortingStr(n))
### leetcode 4 + 451





### leetcode 179 最大数
from typing import List
import functools
class Solution:
    #先把nums中的所有数字转化为字符串，形成字符串数组 nums_str
    #比较两个字符串x,y的拼接结果x+y和y+x哪个更大，从而确定x和y谁排在前面；将nums_str降序排序
    #把整个数组排序的结果拼接成一个字符串，并且返回
    def largestNumber(self, nums: List[int]) -> str:
        nums_str=list(map(str,nums))
        compare=lambda x,y: 1 if x+y<y+x else -1
        nums_str.sort(key=functools.cmp_to_key(compare))
        res=''.join(nums_str)
        if res[0]=='0':
            res='0'
        return res
        
    def largestNumber(self, nums: List[int]) -> str:
        lt = list(map( str, nums))
        def cmp(x, y):
            if x+y < y+x:
                return 1
            else:
                return -1
        lt.sort(key =  functools.cmp_to_key(cmp))
        res = ""
        for i in lt:
            res+=i
        if res[0] == "0":
            return "0"
        return res

### leetcode 3 无重复字符的最长子串 (滑动窗口)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, dic, res = -1, {}, 0
        for i, c in enumerate(s):
            if c in dic and dic[c] > k:
                k = dic[c]
                dic[c] = i
            else:
                dic[c] = i
                res = max(res, i - k)
        return res

### leetcode 5 最长回文字符串

class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break
                    
                if s[i] != s[j]:
                    dp[i][j] = False 
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]

### 牛客 字符串排序
def working(s: str):
    xs = list(s)
    n = len(xs)
    res = []
    for i in xs:
        if i.isalpha():
            res.append(i)
    res.sort(key = str.upper)
    j = 0
    for i in range(n):
        if xs[i].isalpha():
            xs[i] = res[j]
            j += 1
    
    return print("".join(xs))


while 1:
    try:
        s = input()
        working(s)
    except:
        break