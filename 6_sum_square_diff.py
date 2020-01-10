def sum_square_diff(n):
    squared_sum = n * (n + 1) / 2
    squared_sum = squared_sum ** 2

    sum_of_squares = (n * (2*n**2 + 3*n + 1)) / 6

    return int(squared_sum - sum_of_squares)

print(sum_square_diff(100))