#!/usr/bin/python3
"""Pascal's Triangle Module"""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
            Each inner list represents a row of the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        row = triangle[-1]
        new_row = [1]
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
