#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for line in matrix:
        squared.append([elm**2 for elm in line])
    return squared
