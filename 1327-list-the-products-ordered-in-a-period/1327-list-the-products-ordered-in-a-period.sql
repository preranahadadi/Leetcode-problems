# Write your MySQL query statement below
Select product_name , sum(unit) as unit  
From Products  p
Inner Join Orders o
on p.product_id = o.product_id
where order_date LIKE '2020-02-%'
Group by o.product_id
Having sum(unit)>=100