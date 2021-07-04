select * from employees 
where hire_date = 
(select max(hire_date) from employees)

最晚入职员工




select * from employees 
where hire_date = 
(select distinct hire_date 
 from employees
 order by hire_date DESC
 limit 1 offset 2

)

入职时间第三短



select s.*,d.dept_no
from salaries as s , dept_manager as d
on s.emp_no=d.emp_no
order by s.emp_no asc
合并表格

select s.last_name,s.first_name,d.dept_no 
from employees as s ,dept_emp as d
where s.emp_no = d.emp_no

select s.last_name,s.first_name,d.dept_no 
from employees as s 
left outer join dept_emp as d
on s.emp_no = d.emp_no

##outer join 保持多余的并用null/none 补充



select emp_no, count(emp_no) as t
from salaries
group by emp_no having t> 15
## 聚类并选择

select emp_no from employees 
where emp_no not in (select emp_no from dept_manager)
选择两个表的数据差



