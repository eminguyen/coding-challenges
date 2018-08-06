/*
 * Problem: 
 *
 * The Employee table holds all employees including their managers.
 * Every employee has an Id, and there is also a column for the manager Id.
 *
 * Given the Employee table, write a SQL query that finds out employees who 
 * earn more than their managers. For the above table, Joe is the only employee 
 * who earns more than his manager.
 */

# Write your MySQL query statement below
SELECT 
    a.name AS 'Employee'
FROM
    Employee as a,
    Employee as b
WHERE
    a.ManagerId = b.Id AND a.Salary > b.salary;
