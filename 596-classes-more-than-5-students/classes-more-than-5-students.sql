# Write your MySQL query statement below
WITH classes_with_5_students AS (
    SELECT COUNT(student) AS student_count, class
        FROM Courses
        GROUP BY class
        HAVING student_count >= 5
)

SELECT class
    FROM classes_with_5_students;