CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
    SET M = N -1;
  RETURN (
      SELECT (
            SELECT DISTINCT e.salary
                FROM Employee as e
                ORDER BY e.salary DESC
                LIMIT 1 OFFSET M
        )
 );
END