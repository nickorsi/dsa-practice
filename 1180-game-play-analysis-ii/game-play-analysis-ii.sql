# Write your MySQL query statement below
SELECT player_id, device_id
    FROM Activity
    WHERE (player_id, event_date) in 
        (SELECT player_id, min(event_date)
            FROM Activity
            GROUP BY player_id);

-- WITH first_device_login as (
--     SELECT 
--     player_id, 
--     device_id, 
--     RANK() OVER(
--         PARTITION BY 
--             player_id 
--             ORDER BY 
--             event_date asc
--     ) AS rnk 
--     FROM 
--         Activity
-- )

-- SELECT player_id, device_id
--     FROM first_device_login
--     WHERE rnk = 1;