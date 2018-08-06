/* 
 * Problem:
 *
 * There is a table World
 * 
 * A country is big if it has an area of bigger than 3 million square km or a population of more than 25 million.
 * Write a SQL solution to output big countries' name, population and area.
 */

# Write your MySQL query statement below
SELECT
    name,population,area
FROM 
    World
WHERE 
    population > 25000000 OR area > 3000000;
