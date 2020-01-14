'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find_special_triple():
    for a in range(3, 201):
        if 1000 * (a - 500) % (a - 1000) == 0:
            b = int(1000 * ((a - 500) / (a - 1000)))
            c = int(1000 - a - b)
            print(a, b, c)
            return a*b*c

if __name__ == '__main__':
    print(find_special_triple())