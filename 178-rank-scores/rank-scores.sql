# Write your MySQL query statement below
-- SELECT s.score,
--     (
--         SELECT COUNT(DISTINCT t.score)
--             FROM Scores AS t
--             WHERE t.score >= s.score
--     ) AS 'Rank'
--     FROM Scores as s
--     ORDER BY s.score DESC;

SELECT s.score, DENSE_RANK() OVER( ORDER BY s.score DESC) AS 'Rank'
    FROM Scores AS s;