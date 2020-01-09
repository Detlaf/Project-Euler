def sum_square_diff():
    sum_of_squares = 0
    squared_sum = 0
    for i in range(1, 101):
        sum_of_squares += i ** 2
        squared_sum += i
    squared_sum = squared_sum ** 2

    return (squared_sum - sum_of_squares)

print(sum_square_diff())