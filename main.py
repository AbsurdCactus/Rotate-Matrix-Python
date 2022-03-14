
def rotate_matrix(given_matrix):

    n = len(given_matrix)

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1

        for i in range(first, last):
            
            top = given_matrix[layer][i]

            # left to top
            given_matrix[layer][i] = given_matrix[-i - 1][layer]

            # bottom to left
            given_matrix[-i - 1][layer] = given_matrix[-layer - 1][-i - 1]

            # right to bottom
            given_matrix[-layer - 1][-i - 1] = given_matrix[i][-layer - 1]

            # top to right
            given_matrix[i][-layer -1] = top # right is the saved top from earlier.
    return given_matrix