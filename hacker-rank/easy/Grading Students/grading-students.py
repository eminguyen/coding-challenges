"""
Problem:

Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
"""

#!/bin/python3

import os
import sys
import math

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    finalGrades = []
    for grade in grades:
        nextMultiple = 5 * math.ceil(grade / 5)
        if nextMultiple - grade < 3 and nextMultiple >= 40:
            finalGrades.append(nextMultiple)
        else:
            finalGrades.append(grade)
    return finalGrades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
