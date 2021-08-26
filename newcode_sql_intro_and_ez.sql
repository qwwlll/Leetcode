"""
SQL77 牛客的课程订单分析(一)
date > x| name in( , , )
select * from order_info where date > '2025-10-15' and product_name in ('C++','Java','Python') and status = 'completed'order by id
"""



"""
SQL72 考试分数(一)
select job, round(Avg(score),3) as avg from grade group by job order by avg DESC
round(x,3)
"""


"""
SQL66 牛客每个人最近的登录日期(一)
select user_id, max(date) as d from login group by user_id ORDER by user_id
"""

"""
SQL64 找到每个人的任务
select person.id,person.name,task.content from person left join task on person.id=task.person_id order by person.id
"""


"""
SQL62 出现三次以上相同积分的情况
having count
select number from grade where number having count(number) > 3 
"""

"""
SQL45 将titles_test表名修改为titles_2017
ALTER TABLE 表名 ADD 列名/索引/主键/外键等；
ALTER TABLE 表名 DROP 列名/索引/主键/外键等；
ALTER TABLE 表名 ALTER 仅用来改变某列的默认值；
ALTER TABLE 表名 RENAME 列名/索引名 TO 新的列名/新索引名；
ALTER TABLE 表名 RENAME TO/AS 新表名;
ALTER TABLE 表名 MODIFY 列的定义但不改变列名；
ALTER TABLE 表名 CHANGE 列名和定义都可以改变。
alter TABLE titles_test RENAME to titles_2017
"""



"""
SQL44 将id=5以及emp_no=10001的行数据替换成
update_set_replace
update titles_test
set emp_no = replace(emp_no,10001,10005) where id = 5
"""


"""
SQL43 update
update titles_test
set to_date = NULL ,from_date = '2001-01-01'
where to_date = '9999-01-01'
"""


"""
SQL42 删除emp_no重复的记录，只保留最小的id
delete 

delete from titles_test
where id not in(
select min_id from 
    (select min(id) as min_id from titles_test group by emp_no)t1);
"""



"""
SQL34 批量插入数据


insert values()
INSERT INTO actor
VALUES (1, 'PENELOPE', 'GUINESS', '2006-02-15 12:34:33'),
       (2, 'NICK', 'WAHLBERG', '2006-02-15 12:34:33');
       
"""


"""
SQL32 concat
SELECT CONCAT(last_name, ' ', first_name)Name FROM employees;
"""


"""
SQL17 获取当前薪水第二多的员工

limit 1, 1  ////  distinct
select emp_no, salary
from salaries
where salary = 
    (select distinct salary 
        from salaries 
        order by salary desc 
        limit 1,1
    );
"""





"""
SQL 17: 查找employees表所有emp_no为奇数，且last_name不为Mary的员工信息
补充：sql中/表示标准除法，如101/2得到50.5，而DIV表示整数除法，如101 DIV 2得到50

补充：奇偶数查询：参考资料：https://blog.csdn.net/ccStroy/article/details/78061861
查询奇数的一般方法：如上(最好是位运算&)
查询偶数的一般方法：emp_no=(emp_no>>1<<1)
但是，以上的一般方法，针对的是字段全是数字的情况，如果对于身份证这种中间隐藏了一部分的，积极无法使用
所以更好的方法是使用正则化表达式(当然题库这里无法使用正则化表达式，可能是版本或设置问题)
查询奇数的正则化方法：emp_no REGEXP ‘[13579]’
注意：表示以13579中的任意一个结尾
补充：顺便说一下正则化表达式：
^aa：以aa开头
aa$：以aa结尾
.：匹配任何字符
[abc]：[字符集合]，包含中括号内的字符
[^abc]或[!abc]：[字符集合]，不包含中括号内的字符
a|b|c：匹配a或b或c，如(中|美)国
：匹配前面的子表达式0次或者多次。如，zo能匹配’z’以及’zoo’。*等价于{0,}
+：匹配前面的子表达式1次或者多次。如，’zo+’能匹配’zo’，但不能匹配’z’。+等价于{1,}
{n}：n是一个非负整数，匹配前面的子表达式2次。如，o{2} 能匹配’food’中的两个o，但不能匹配’Bob’中的o
{n, m}：m和n均为非负整数，其中n<=m。最少匹配n次且最多匹配m次。




SELECT * from employees 
where emp_no%2 != 0 and last_name != 'Mary'
order by hire_date DESC
"""


"""
SQL10 获取所有非manager的员工emp_no

not in

SELECT emp_no from employees
where emp_no not in (select emp_no from dept_manager)
"""

"""
SQL8 找出所有员工当前薪水salary情况
distinct

SELECT DISTINCT salary from salaries order by salary DESC
"""




"""
SQL4 查找所有已经分配部门的员工
join


SELECT employees.last_name, employees.first_name, dept_emp.dept_no 
from employees  join  dept_emp on employees.emp_no = dept_emp.emp_no
"""