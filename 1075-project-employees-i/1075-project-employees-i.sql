# Write your MySQL query statement below
Select project_id , 
ROUND(AVG(e.experience_years),2) as average_years
FROM Project p 
LEFT JOIN Employee E
on p.employee_id = e.employee_id
GROUP BY project_id
