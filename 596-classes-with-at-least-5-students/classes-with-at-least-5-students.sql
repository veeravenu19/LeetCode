# Write your MySQL query statement below


select class from
(select class,count(*) as a from Courses
group by class) as b
where a >=5