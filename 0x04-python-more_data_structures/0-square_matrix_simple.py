#!/usr/bin/python3

##Write a function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    return [list(map((lambda x: x * x), element)) for element in matrix]