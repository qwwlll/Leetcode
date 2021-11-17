### leetcode 344 翻转字符串
### 你必须原地修改输入数组
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        h = n//2
        for i in range(h):
            s[i], s[n-1-i] = s[n-i-1],s[i]



### leetcode 151 翻转字符串里的单词
#输入：s = "the sky is blue"
#输出："blue is sky the"
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        b = reversed(a)
        c = " ".join(b)
        return c





###leetcode 8 字符串转整数
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647    
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值
#^：匹配字符串开头
#[\+\-]：代表一个+字符或-字符
#?：前面一个字符可有可无
#\d：一个数字
#+：前面一个字符的一个或多个
#\D：一个非数字字符
#*：前面一个字符的0个或多个