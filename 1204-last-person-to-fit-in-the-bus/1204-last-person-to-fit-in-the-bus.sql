# Write your MySQL query statement below
With cumulative AS (
    Select 
    person_name , weight ,turn,
    SUM(Weight) OVER (order by turn) as running_total
    from queue
)
Select person_name
From Cumulative
where running_total <=1000
order by turn desc
limit 1 
