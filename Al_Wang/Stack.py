## 判定括号
##用一个栈 来储存左

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
               
##