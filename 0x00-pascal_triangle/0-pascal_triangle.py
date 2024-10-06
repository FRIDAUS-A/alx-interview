#!/usr/bin/python3
"""
 A module to implement pascal triangle
"""

def pascal_triangle(n):
    """
        This function creates a pascal triangle and returns an empty
        list if n is less than or equals zero
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        line = []
        for j in range(i + 1):
            if i == 0:
                line = [1]
                break
            elif i == 1:
                line = [1, 1]
                break
            if j == 0 or j == i:
                line.append(1)
            else:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)
    return triangle

