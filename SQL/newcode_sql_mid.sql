
"""
SQL89 获得积分最多的人(一)
join

select user.name,t.grade_sum from
(select user_id,sum(grade_num) as grade_sum 
 from grade_info group by user_id order by grade_sum desc limit 1) t
join user
on t.user_id=user.id
"""

"""
SQL87 最差是第几名(一)

sum()over (order by) 累加！！
select grade, sum(number) over (order by grade) t_rank
from class_grade order by grade 
"""



"""
SQL85 实习广场投递简历分
date_format()
like '2025%'
group by x , x
order by x desc, x desc

SELECT job, DATE_FORMAT(date,'%Y-%m') as mon, sum(num) as cnt 
from resume_info 
where date like '2025%'
group by job, mon order by mon DESC,cnt DESC
"""


"""
SQL79


group by 只会返回第一行数据
窗口函数是对where或者group by子句处理后的结果进行操作，不可在一次查询中对窗口函数的结果进行操作
窗口函数:
https://zhuanlan.zhihu.com/p/92654574
SELECT * from order_info 
WHERE date > '2025-10-15' and product_name in ('Java','Python','C++')
and status = 'completed'
and user_id in (
                select user_id from order_info 
                where date > '2025-10-15'
                and product_name in ('C++','Java','Python')
                and status = 'completed'
                group by user_id
                having count(user_id)>=2
)
ORDER by id
"""



"""
SQL 82
"""



"""
SQL 78

    select user_id from order_info
    where date > '2025-10-15'and product_name in ('Python','C++','Java')
    and status = 'completed' group by user_id having count(user_id)>1 
    order by user_id


"""


"""
SQL73
建立新表 
left join
print 旧表全部 
grade.*

select grade.* from grade 
left join (
SELECT job, avg(score) as Av_num from grade group by job
) as Av
on grade.job = Av.job
where grade.score > Av.Av_num
order by grade.id

"""



"""
SQL63 刷题通过的题目排名
row_number：不考虑并列的情况，哪怕分数相同，排名都是一溜下来的自然数。
dense_rank和rank 考虑并列的情况，区别在于rank很跳，并列排名的个数会影响接下来的排名，表现为数字的中断。
而dense_rank 不管有几个并列的第5名，接下来都是从6开始排。

SELECT id ,number, DENSE_RANK() over(order by number desc) as t_rank
from passing_number
"""



"""
SQL57 使用含有关键字exists查找未分配具体部门


EXISTS语句：执行employees.length次
指定一个子查询，检测行的存在。遍历循环外表，然后看外表中的记录有没有和内表的数据一样的。匹配上就将结果放入结果集中。

IN 语句：只执行一次 感觉看起来更通俗易懂
确定给定的值是否与子查询或列表中的值相匹配。
in在查询的时候，首先查询子查询的表，然后将内表和外表做一个笛卡尔积，然后按照条件进行筛选。所以相对内表比较小的时候，in的速度较快。

SELECT * from employees 
where not EXISTS (select emp_no from dept_emp
                         where dept_emp.emp_no = employees.emp_no
               )
"""


"""
SQL55 limit
LIMIT 语句结构： LIMIT X,Y 
Y ：返回几条记录
X：从第几条记录开始返回（第一条记录序号为0，默认为0）

SELECT *
FROM employees
LIMIT 5,5

"""



"""
SQL54 查找排除当前最大、最小salary之后的员工
not in 

select avg(salary) as avg_salary from salaries
where  to_date = '9999-01-01' and salary not in(
    select max(salary) from salaries where to_date = '9999-01-01') 
    and  salary not in (select min(salary) from salaries where to_date = '9999-01-01')
"""


"""
SQL53 按照dept_no进行汇总
group_concat()


SELECT dept_no,group_concat(emp_no) employees
FROM dept_emp GROUP BY dept_no
"""


"""
SQL52 获取Employees中的first_name
right / left(name, 2)
substr(name, -2)
SELECT first_name from employees order by right (first_name, 2)
SELECT first_name FROM employees ORDER BY substr(first_name,-2)
"""


"""
SQL51 查找字符串 10,A,B 中逗号,出现的次数cnt
char_length 
replace
select char_length("10,A,B")-char_length(replace("10,A,B",",",""))
"""

"""
SQL50 
concat(x, y, z)
SELECT CONCAT(last_name,"'",first_name) as name from employees
"""

"""
SQL48 将所有获取奖金的员工当前的薪水增加10%


update table
set ....

update salaries
set salary = salary*1.1 where to_date = '9999-01-01'
and emp_no in (select emp_no from emp_bonus)
"""

"""
SQL46 在audit表上创建外键约束
创建外键语句结构：
ALTER TABLE <表名>
ADD CONSTRAINT FOREIGN KEY (<列名>)
REFERENCES <关联表>（关联列）

ALTER TABLE audit
ADD CONSTRAINT FOREIGN KEY (emp_no)
REFERENCES employees_test(id);
"""

"""
SQL41 触发器
在MySQL中，创建触发器语法如下：
CREATE TRIGGER trigger_name
trigger_time trigger_event ON tbl_name
FOR EACH ROW
trigger_stmt
其中：

trigger_name：标识触发器名称，用户自行指定；
trigger_time：标识触发时机，取值为 BEFORE 或 AFTER；
trigger_event：标识触发事件，取值为 INSERT、UPDATE 或 DELETE；
tbl_name：标识建立触发器的表名，即在哪张表上建立触发器；
trigger_stmt：触发器程序体，可以是一句SQL语句，或者用 BEGIN 和 END 包含的多条语句，每条语句结束要分号结尾。

CREATE TRIGGER audit_log 
AFTER INSERT ON employees_test
FOR EACH ROW
BEGIN
    INSERT INTO audit VALUES(new.id,new.name);
END


"""



"""
SQL40
alter table添加表列的语法:
ALTER TABLE table_name
ADD column_name datatype;

alter TABLE actor
add create_date datetime not null default "2020-10-01 00:00:00"
"""

"""
SQL39

强制索引FORCE INDEX
FORCE INDEX强制查询优化器使用指定的命名索引。查询优化器是MySQL数据库服务器中的一个组件，它为SQL语句提供最佳的执行计划。
查询优化器使用可用的统计信息来提出所有候选计划中成本最低的计划。
书写顺序;
SELECT……
FROM ……
FORCE INDEX(index_name)
WHERE……

SELECT  *
  FROM salaries
  FORCE INDEX(idx_emp_no)
  WHERE emp_no = 10005;
"""

"""
SQL36 创建一个actor_name表

create table if not exists actor_name(
first_name  varchar(45)  not null,
last_name   varchar(45)  not null); -- 创建表

insert into actor_name
select     first_name,last_name
from actor; -- 插入查询结果
"""


"""
SQL30 使用子查询的方式找出属于Action分类
双子查询

select title, DESCRIPTION from film 
where film_id in (
select film_id 
from film_category 
where category_id = 
(select category_id from category where name = 'action'))
"""


"""
SQL29 使用join查询方式找出没有分类的电影id
left_join

SELECT film.film_id, film.title from film 
left join film_category on 
film.film_id = film_category.film_id
where film_category.category_id is null
"""


"""
SQL22 统计各个部门的工资记录数


join +join

select departments.dept_no, departments.dept_name, A.sum
from departments left join
(select dept_emp.dept_no, count(dept_emp.dept_no) as sum 
 from salaries  
left join dept_emp on salaries.emp_no = dept_emp.emp_no group by dept_emp.dept_no
) A 
on departments.dept_no = A.dept_no

"""


"""
SQL19


select em.last_name, em.first_name, A.dept_name from employees em left join
(SELECT de.dept_name,d.emp_no from departments de left join 
dept_emp d on d.dept_no = de.dept_no) A
on em.emp_no = A.emp_no

"""


"""
SQL16
join + avg

SELECT t.title, avg(sa.salary)from titles t left join 
salaries sa on t.emp_no = sa.emp_no
group by t.title
"""


"""
SQL11 获取所有员工当前的manager

SELECT de.emp_no ,dm.emp_no from dept_emp de left JOIN
dept_manager dm on de.dept_no = dm.dept_no
where de.emp_no != dm.emp_no
"""


"""
SQL05
join

SELECT e.last_name, e.first_name, de.dept_no from employees e left JOIN
dept_emp de on e.emp_no = de.emp_no 
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