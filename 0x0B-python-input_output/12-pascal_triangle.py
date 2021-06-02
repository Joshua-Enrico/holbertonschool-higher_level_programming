#!/usr/bin/python3
"""
triangule pascal function
"""


def pascal_triangle(n):
    """returns triangule pascal representation"""
    if n <= 0:
        return []

    limit = n - 1
    area = [[1]]

    for i in range(limit):
        row = []
        row.append(1)

        if len(area[i]) > 1:
            prev_l = len(area[i]) - 1
            next = 1

            for b in range(prev_l):
                sum = area[i][b] + area[i][next]
                row.append(sum)
                next += 1

        row.append(1)
        area.append(row)
    return area
