"""
#不用库 取立方根（二分法）
def cube(num):
   
    if num == 0:
        return 0
    if num > 0:
        sig = 1
    else:
        sig = -1
    num = abs(num)

    if num > 1:
        start = 0
        end = num
    else:
        start = num
        end = 1
    mid = (end + start) / 2
    while abs(mid ** 3 - num) > 0.001:
        if mid ** 3 > num:
            end = mid
        else:
            start = mid
        mid = (end + start) / 2
    return (round(sig * mid, 1))
  
while True:
    try:
        num = float(input())
        print(cube(num))
    except:
        break
"""
"""


x(n+1) = x(n) - f(xn)/f'(xn)


牛顿渐进
n= float(input())
x=1
while abs(x**3-n)>0.001:
    x=x-(x**3-n)/(3*x**2)
print(round(x,1))




n= float(input())
x=1
while abs(x**2-n)>0.001:
    x=x-(x**2-n)/(2*x)
print(round(x,1))
"""


"""
#不用库取平方根

def squ():
    a = float(input("insert number to take square: "))
    if a < 0:
        a = abs(a)
    start = 0
    end = a
    mid = (start + end) /2
    if a > 0 and a < 1:
        start = 0
        end = 1
        mid = (start + end)/2
    if a >=0:
        while abs(mid ** 2 - a) > 0.001:
            if a > 1:
                if mid ** 2 > a:
                    end = mid
                else:
                    start = mid 
                mid = (start + end )/2
            elif a == 0 or a == 1:
                mid = mid
            else:
                if mid ** 2 > a:
                    
                    end = mid
                else:
                    start = mid 
                mid = (start + end )/2
                
    return(round(mid, 1))
                    
while True:
    try:
        print(squ())
    except:
        break
"""

"""
SQL07查找薪水记录超过15次的员工号emp_no以及其对应的记录次数t

实际上group by 后面直接加having是可以的。重新复习了一下知识点：
groupby子句常见错误
1）SELECT 子句中只能存在以下三种 元素。
●常数 ● 聚合函数 ● GROUP BY子句中指定的列名（也就是聚合键）
2）where子句中不能使用聚合函数
聚合函数可以再select,having,order by之后出现
where指定分组之前数据行的条件，having子句用来指定分组之后条件

SELECT emp_no, count(salary) as t from salaries group by emp_no having t > 15\

"""


"""



"""