class Solution:
    def Fibonacci(self, n):
        # write code here
        res = 0
        if n == 0:
            res = 0
            return res 
        elif n == 1:
            res = 1
            return res 
        elif n == 2:
            res = 1
            return res
        else:
            res = self.Fibonacci(n-1) + self.Fibonacci(n-2)
            return res
       
    def Finboacci_1(self,n):
        if n == 0:
            return n

        n1, n2 = 1, 1
        count = 2

        while count < n:
            n1, n2 = n2, n1 + n2
            count += 1
        return n2




    def gcd(self , a , b ):
        # write code here
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a%b)


    def Judge(self, str):
        #判断回文
        return str == str[::-1]



    def solve(self , a ):
        #寻找缺失的数字

        for i in range(len(a)):
            if i != a[i]:
                return i
            elif i == a[-1]:
                return len(a) 


    def solve(self , a ):
        # write code here
        # 寻找最高的山峰
        lt = []
        for i in range (1,len(a)-1):
            if a[0]> a[1]:
                lt.append(0)
            if a[-1]>a[-2]:
                lt.append(len(a)-1)
            elif a[i]>a[i-1] and a[i]> a[i+1]:
                lt.append(i)
        
        return (max(lt))



    def spiralOrder(self,matrix):
        # write code here
        #螺旋矩阵排列
        num = 1 
        i = 0
        j = 0
        move_dir = 1 # 1-right, 2-down, 3-left, 4-up
        m = len(matrix)
        if m == 0:
            n = 0
        else:
            n = len(matrix[0])
        visited = []
        while num <= m * n :
            visited.append(matrix[i][j])
            if move_dir == 1 and i+j == n-1 : #turning point
                move_dir = 2
            elif move_dir == 2 and m-i == n-j:#turning point
                move_dir = 3
            elif move_dir == 3 and i + j == m -1:#turning point
                move_dir = 4
            elif move_dir == 4 and i - j == 1:#turning point
                move_dir = 1
            if move_dir == 1:
                j += 1
            elif move_dir == 2:
                i += 1
            elif move_dir == 3:
                j -= 1
            elif move_dir == 4:
                i -= 1
            num += 1
        return visited
