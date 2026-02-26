# Write your MySQL query statement below
Select 
LEFT(trans_date,7) AS month,
country,
count(*) as trans_count,
SUM(CASE WHEN state='approved' THEN 1 else 0 END)as approved_count,
SUM(amount) as trans_total_amount,
SUM(CASE WHEN state='approved' THEN AMOUNT ELSE 0 END)as approved_total_amount
FROM Transactions
Group by LEFT(trans_date,7),country;