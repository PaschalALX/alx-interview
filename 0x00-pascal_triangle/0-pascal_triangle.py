#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    result = []
    if n > 0:
        for x in range(1, n + 1):
            row = list(x**0 for x in range(x))
            try:
                prev_row = result[-1]
                for y in range(len(prev_row)):
                    try:
                        row[y + 1] = prev_row[y] + prev_row[y + 1]
                    except IndexError:
                        row[y + 1] = prev_row[y]
                result.append(row)
            except IndexError:
                result.append(row)
    return result
