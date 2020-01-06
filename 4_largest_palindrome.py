'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def get_reverse(number):
    digits = []
    divisor = 100000
    n = number
    for i in range(6):
        digits.append(n // divisor)
        n -= digits[i] * divisor
        divisor /= 10
    multi = 1
    reverse = 0
    for x in digits:
        reverse += x * multi
        multi *= 10
    return int(reverse)

def largest_palindrome():
    max_palindrom = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            product = i * j
            reverse = get_reverse(product)
            if product == reverse:
                if product > max_palindrom:
                    max_palindrom = product
    return max_palindrom


print(largest_palindrome())