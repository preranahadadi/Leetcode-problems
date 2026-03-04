# Write your MySQL query statement below
Select 
id ,
count(id) AS num
From 
( select requester_id as id
from RequestAccepted
UNION ALL
Select accepter_id as id
from RequestAccepted
)AS t
Group by id
order by num desc
limit 1;