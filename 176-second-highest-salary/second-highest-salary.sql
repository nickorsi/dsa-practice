# Write your MySQL query statement below
SELECT Max(e.salary) AS SecondHighestSalary
    FROM Employee as e
    WHERE e.salary < (
        SELECT Max(e.salary) as highes_salary
        FROM Employee as e
    );