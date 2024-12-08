# Write your MySQL query statement below
-- Find all order id's where they relate to company name red
-- Above with establish all id's we don't want
-- Find all order_id not in the above
-- Return all names associated with the above id's

SELECT s.name FROM SalesPerson AS s
    -- LEFT JOIN Orders AS o
    -- ON s.sales_id = o.sales_id
    WHERE s.sales_id NOT IN 
        (SELECT o.sales_id FROM Orders AS o
            JOIN Company AS c
            ON o.com_id = c.com_id
            WHERE c.name = "RED");