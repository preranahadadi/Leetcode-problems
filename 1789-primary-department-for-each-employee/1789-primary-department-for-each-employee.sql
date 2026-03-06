# Write your MySQL query statement below
Select employee_id , department_id
from Employee
where primary_flag = 'Y'
OR employee_id in 
(select employee_id
From employee
Group by employee_id
having count(*) =1 )
