# Write your MySQL query statement below
with cte as (

select id, num, 
lag(num, 1) over (order by id) as prev_num,
lead(num, 1) over (order by id) as next_num 

from Logs
)

select distinct num as ConsecutiveNums from cte where num = next_num and num = prev_num
