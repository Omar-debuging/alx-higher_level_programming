def square_matrix_map(matrix=[]):
    result = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    print(result)
