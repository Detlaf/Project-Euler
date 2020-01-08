'''
What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

In order to be divisible by 5 the number must end in 0 or 5. 
The number has to be even otherwise it is not divisible by 6.
'''

def check_divisible(n):
    for d in range(2, 20):
        if n % d != 0:
            return False
    return True

num = 20
while True:
    if check_divisible(num):
        break
    else:
        num += 10
print(num)
