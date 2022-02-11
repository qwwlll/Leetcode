
#SQL1 查找最晚入职员工的所有信息
select * from employees where hire_date = (select max(hire_date) from employees)


#SQL2 请你查找employees里入职员工时间排名倒数第三的员工所有信息
SELECT * from employees 
where hire_date = 
(select distinct hire_date 
 from employees order by hire_date desc limit 2, 1)

#SQL3 查找当前薪水详情以及部门编号dept_no
select s.*, d.dept_no
from  salaries s join dept_manager d
on s.emp_no = d.emp_no
order by s.emp_no ASC 

#SQL4 请你查找所有已经分配部门的员工的last_name和first_name以及dept_no
SELECT e.last_name, e.first_name, d.dept_no
from employees e join dept_emp d ON e.emp_no = d.emp_no
ORDER by e.emp_no ASC


#SQL5 请你查找所有已经分配部门的员工的last_name和first_name以及dept_no
SELECT e.last_name, e.first_name, d.dept_no 
from employees e left join dept_emp d 
on e.emp_no = d.emp_no

-- INNER JOIN 两边表同时有对应的数据，即任何一边缺失数据就不显示。
-- LEFT JOIN 会读取左边数据表的全部数据，即便右边表无对应数据。
-- RIGHT JOIN 会读取右边数据表的全部数据，即便左边表无对应数据。

#SQL7 请你查找薪水记录超过15次的员工号emp_no以及其对应的记录次数t
SELECT emp_no,count(emp_no) as t from salaries
group by emp_no having t > 15

-- 还有就是group by与order by有什么区别，order by就是排序。而group
-- by就是分组，举个例子好说点，group by 单位名称 

-- 这样的运行结果就是以“单位名称”为分类标志统计各单位的职工人数和工资总额。

-- 这样可以更好的分下类，更好看一些。

-- 还有就是为什么没有用where而是用的having，记住下面的两句话就好了。


-- WHERE语句在GROUP BY语句之前；SQL会在分组之前计算WHERE语句。   

-- HAVING语句在GROUP BY语句之后；SQL会在分组之后计算HAVING语句。

#SQL8 找出所有员工当前薪水salary情况
select DISTINCT salary from salaries order by salary DESC

SQL10 获取所有非manager的员工emp_no