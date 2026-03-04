# Write your MySQL query statement below
Select user_id,
    Concat(Upper(substring(name,1,1)),LOWER(SUBSTRING(name,2)))
As name  
from Users
Order by user_id 
