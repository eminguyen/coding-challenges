/*
 * Problem:
 *
 * Write a SQL query to find all duplicate emails in a table named Person.
 */
 
# Write your MySQL query statement below
SELECT
    Email
FROM 
    Person
GROUP BY
    Email
HAVING 
    COUNT(Email) > 1;
