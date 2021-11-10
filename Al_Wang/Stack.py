#####20,155,232,844,224,682,496


## 判定括号
##用一个栈 来储存左
#######Leetcode 20
class Solution:
    def isValid(self , s: str) -> bool:
        # write code here
        if len(s) % 2 == 1:
            return False
        stack = list()
        for a in s:
            if a == "(" or a == "{" or a == "[":
                stack.append(a)
            else:
                if not stack: ## 非空
                    return False
                top = stack[-1]
                stack.pop()  ##删除顶部
                if a == "}" and top !="{":  ##判断另一边
                    return False
                if a == ")" and top !="(":
                    return False
                if a == "]" and top !="[":
                    return False
        return not stack ## 判断是否空
               
## 最小栈
#######Leetcode 155
## 时间复杂度 O(1)
import math
class Solution:
    def __init__(self):
        self.st = []
        ## 要比较大小，在初始化的时候保持mini 里面是正无穷大
        self.mini = [math.inf]

        
    def push(self, node):
        # write code here
        ## 在插入时比较始终保持最小的在top
        self.st.append(node)
        ## 初始化一直保持正无穷大
        self.mini.append(min(node, self.mini[-1]))

    def pop(self):
        # write code here
        self.st.pop()
        self.mini.pop()
    def top(self):
        # write code here
        return self.st[-1]
    def min(self):
        return self.mini[-1]
        # write code here



##退格字符
##leetcode 844
## 用 stack 来储存
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ## 无 self 这里！
        def de(s:str) -> str:
            stack = list()
            for i in s:
                if i != "#":
                    stack.append(i)

                elif stack: ## 当stack 不为空时
                    stack.pop()
            return "".join(stack)

        return de(s) == de(t)

##leetcode 224
##leetcode 232
##leetcode 682
##leetcode 496