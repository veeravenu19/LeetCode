# Write your MySQL query statement below


select id from
(select id,recordDate, temperature, lag(temperature) over(order by recordDate) as prev,

case
when datediff(recordDate, lag(recordDate) over(order by recordDate)) = 1 then 1
else 0
END AS A

 from Weather) as temp
where temperature > prev and A =1



