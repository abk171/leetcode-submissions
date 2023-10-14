# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary
from department d, employee e
where d.id = e.departmentId 
and (e.departmentId, e.salary) in
(select departmentId, max(salary) 
 from employee
group by departmentId)
