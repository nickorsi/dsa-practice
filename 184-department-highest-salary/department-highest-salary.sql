# Write your MySQL query statement below
-- First find the query to determine the max salaries for each department
-- Then use this to find where employees by deparment have salaries and ID's are in this table
SELECT d.name AS Department, e.name AS Employee, Salary
FROM Employee AS e
JOIN Department AS d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN 
(
    SELECT e.departmentId, Max(e.salary) As Salary
    FROM Employee as e
    GROUP BY departmentId
); 
