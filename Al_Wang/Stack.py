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

##leetcode 224 简单计算器
    def solve(self, s):
        # write code here
        def eva(s):
            stack = []
            num = 0 
            sign = "+"
            while len(s) > 0 :
                x = s.pop(0)
                if x.isdigit():
                    num = num * 10 + int(x)
                if x == "(":
                    num = eva(s)
                if ((not x.isdigit()) and x != " ") or len(s) == 0 :
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    num = 0 
                    sign = x
                if x == ")":
                    break
            return sum(stack)
        return eva(list(s))

### edited with * and /
class Solution:
    def solve(self, s):
        # write code here
        def eva(s):
            stack = []
            num = 0 
            sign = "+"
            while len(s) > 0 :
                x = s.pop(0)
                if x.isdigit():
                    num = num * 10 + int(x)
                if x == "(":
                    num = eva(s)
                if ((not x.isdigit()) and x != " ") or len(s) == 0 :
                    if sign == "+":
                        stack.append(num)
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        temp = stack.pop()
                        stack.append(temp * num)
                    elif sign =="/":
                        temp = stack.pop()
                        stack.append(temp/float(num))
                    num = 0 
                    sign = x
                if x == ")":
                    break
            return sum(stack)
        return eva(list(s))
                    

##leetcode 232
##用双栈实现队列
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
       

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]



    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

### leetcode 225
### 用双队列来表示栈
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q2[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q2

##leetcode 682
##leetcode 496