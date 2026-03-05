# Write your MySQL query statement below
Select sell_date , 
Count(Distinct product) as num_sold,
Group_concat(Distinct product order by product Separator ',') AS products
From Activities
Group by sell_date
order By sell_date;
