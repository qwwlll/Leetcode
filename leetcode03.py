class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}  # 空字典
        i = 0    
        ans = 0  #result
        for j in range (len(s)):
            if s[j] in st:
                i = max(st[s[j]],i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans