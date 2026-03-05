# Write your MySQL query statement below
Select(
Select Distinct salary
from
(
Select salary ,
DENSE_RANK() OVER (Order by Salary desc) as rn
from employee ) as rankedsalaries
where rn=2)
AS SecondHighestSalary
