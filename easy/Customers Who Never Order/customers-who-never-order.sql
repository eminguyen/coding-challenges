/*
 * Problem:
 *
 * Suppose that a website contains two tables, the Customers table and the Orders table. 
 * Write a SQL query to find all customers who never order anything.
 */

# Write your MySQL query statement below
SELECT 
    Name AS 'Customers'
FROM
    Customers
WHERE
    Id
NOT IN
    (SELECT CustomerId FROM Orders);
