class Solution:
    def isValid(self, s: str) -> bool:
        while '{}'in s or '()' in s or '[]' in s:
            s = s.replace('{}','')
            s = s.replace('()','')
            s = s.replace('[]','')
        return s == ''
        return True








##        检查是否有完整的括号 有 一个一个去掉 最后return true
