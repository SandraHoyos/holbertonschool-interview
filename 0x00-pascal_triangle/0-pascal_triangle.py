#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(number):
    """calculate pascal if number <= 0 return an empty list"""
    pascal_list = []

    if number <= 0:
        return pascal_list

    for i in range(number):
        temp_list = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                temp_list.append(1)
            else:
                temp_list.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
        pascal_list.append(temp_list)
    return pascal_list
