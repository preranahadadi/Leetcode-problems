# Write your MySQL query statement below
(select u.name as results
From MovieRating m
Join Users u
ON m.user_id = u.user_id
Group by name
Order By count(*) DESC,u.name asc
Limit 1
)
UNION ALL
(Select title as results
From MovieRating mr
Join Movies m
on  m.movie_id = mr.movie_id 
where mr.created_at LIKE '2020-02-%'
group by title
order by avg(mr.rating)desc , m.title ASC
 limit 1 
)