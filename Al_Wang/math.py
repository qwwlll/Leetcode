### leetcode 166. 分数到小数
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        s = []
        if (numerator < 0) != (denominator < 0):
            s.append('-')

        # 整数部分
        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append(str(integerPart))
        s.append('.')

        # 小数部分
        indexMap = {}
        remainder = numerator % denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:  # 有循环节
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)

### leetcode 172. 阶乘后的零
class Solution: ## (会超时)
    def trailingZeroes(self, n: int) -> int:
        res = 1
        for i in range(1,  n+1  ):
            res *= i
        count = 0
        while res % 10 == 0:
            count += 1
            res //= 10
        return count

#### leetcode 29 两数相除c
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        ### 不同符号 
        if dividend ^ divisor < 0 :
            sign = -1
            divisor = abs(divisor)
            dividend = abs(dividend)
        if divisor < 0 and dividend < 0 :
            divisor = abs(divisor)
            dividend = abs(dividend)
        remain = dividend
        result = 0
        while remain >= divisor:
            cur = 1
            div = divisor
            while div + div < remain:
                cur += cur
                div += div
            remain -= div
            result += cur
        if sign == -1:
            result = -result
        
        if result >= 2**31:  
            result = 2**31-1

        return result


#### leetcode 09 回文数
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif str(x) == str(x)[::-1]:
            return True
        else:
            return False
        

#### leetcode 13 罗马数字转整数
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romandic = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M": 1000}
        i , res = 0, 0 
        while i < len(s) - 1:
            if romandic[s[i]] < romandic[s[i + 1]]:
                res -= romandic[s[i]]
            else:
                res += romandic[s[i]]
            i += 1
        return res + romandic[s[-1]]

#### leetcode 12 整数转罗马数字
class Solution:
    def intToRoman(self, num: int) -> str:
        romadic = {"M": 1000, "CM": 900, "D": 500, "CD":400, "C": 100, "XC":90, "L":50, "XL": 40, "X": 10, "IX": 9, "V":5, "IV": 4, "I":1}
        res = []
        for re, val in romadic.items():
            while num >= val:
                num -= val
                res.append(re)
            if num == 0:
                break
        return "".join(res)

