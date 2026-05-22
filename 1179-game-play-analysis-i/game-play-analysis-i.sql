# Write your MySQL query statement below


select player_id, event_date as first_login from
(select player_id,device_id, event_date, games_played, row_number() over(partition by player_id order by event_date) as a from Activity
) as b
where a =1