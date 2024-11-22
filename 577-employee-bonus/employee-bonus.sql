# Write your MySQL query statement below
SELECT e.name, b.bonus
    FROM Employee as e
    LEFT JOIN Bonus as b
        ON e.empId = b.empId
    WHERE b.bonus < 1000 OR b.bonus IS NULL;
    -- WHERE coalesce(b.bonus, 0) < 1000;