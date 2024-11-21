# Write your MySQL query statement below
-- SELECT w1.id as Id
--     FROM Weather as w1
--     JOIN Weather as w2
--     ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
--     WHERE w1.temperature > w2.temperature; 

SELECT w1.id as ID
    FROM Weather as w1, Weather as w2
    WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature;