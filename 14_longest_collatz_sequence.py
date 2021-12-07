def count_collatz_chain(number: int, computed_chain: dict):
    if number in computed_chain.keys():
        return computed_chain[number]

    if number % 2 == 0:
        computed_chain[number] = 1 + count_collatz_chain(number // 2, computed_chain)
    else:
        computed_chain[number] = 2 + count_collatz_chain((3 * number + 1) // 2, computed_chain)

    return computed_chain[number]


if __name__ == '__main__':
    MAX = 1000000000
    longest_chain = 0
    answer = 1
    computed_chain = {1: 1}

    for n in range(MAX // 2, MAX - 1):
        if count_collatz_chain(n, computed_chain) > longest_chain:
            longest_chain = count_collatz_chain(n, computed_chain)
            answer = n
    print(f'Number {answer} produces the longest Collatz chain for numbers under {MAX}')
