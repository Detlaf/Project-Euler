'''
David Gries, Jayadev Misra. A Linear Sieve Algorithm for Finding Prime Numbers
'''

N = 2_000_000
lp = [0 for i in range(N+1)] # minimum prime divisors
pr = [] # prime numbers

for i in range(2, N+1):
    print(i)
    if lp[i] == 0:
        lp[i] = i
        pr.append(i)
    for j in range(len(pr)):
        if pr[j] <= lp[i] and i * pr[j] <= N:
            lp[i * pr[j]] = pr[j]

print('Biggest prime = ', max(pr))
print('Sum of primes = ', sum(pr))