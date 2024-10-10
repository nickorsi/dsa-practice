# Write your MySQL query statement below
-- SELECT e.name as Employee
-- FROM Employee as e
-- JOIN Employee as m
-- ON e.managerID = m.id
-- WHERE e.salary > m.salary;

SELECT e.name AS Employee
FROM 
    Employee AS e, 
    Employee AS m
WHERE e.salary > m.salary AND e.managerId = m.id;