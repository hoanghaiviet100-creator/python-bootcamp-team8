def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a matrix; unlike C++, Python can use zip to group columns."""
    return [list(row) for row in zip(*matrix)]
    """*matrix is unpacking the matrix so that zip() receives row lists from matrix as arguments and not the whole matrix itself"""