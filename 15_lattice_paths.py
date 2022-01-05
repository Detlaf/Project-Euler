import math


def binomial_coeff(n):
    return (math.factorial(2 * n)) // (math.factorial(n) ** 2)


print(binomial_coeff(20))
