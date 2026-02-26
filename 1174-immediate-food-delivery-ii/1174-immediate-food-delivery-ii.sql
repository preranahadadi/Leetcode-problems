# Write your MySQL query statement beloww
WITH first_orders AS(
    Select *, 
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS rn
        From Delivery 
)
SELECT ROUND(
    100*AVG(order_date = customer_pref_delivery_date),2) AS immediate_percentage
FROM first_orders
where rn=1

