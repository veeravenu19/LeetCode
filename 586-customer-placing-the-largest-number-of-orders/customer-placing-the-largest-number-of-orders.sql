# Write your MySQL query statement below


select customer_number from
(select customer_number,count(*) as a from Orders
group by customer_number) as b
order by a desc
limit 1
