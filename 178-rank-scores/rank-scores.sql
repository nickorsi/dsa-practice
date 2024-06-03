-- Write your PostgreSQL query statement below
SELECT s.score, (dense_rank() OVER (ORDER BY s.score DESC)) as Rank
    FROM Scores as s;
