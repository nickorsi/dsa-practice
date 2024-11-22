-- Write your PostgreSQL query statement below
WITH first_device_login as 
    (SELECT player_id, device_id, ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date asc) as row_number  
    FROM Activity)

SELECT player_id, device_id
    FROM first_device_login
    WHERE row_number = 1;