def get_pisano_len(m):
    pisano = [0, 1]
    prev = 0
    current = 1
    for _ in range(2, m*6+2):
        prev, current = current, (prev + current) % m
        pisano.append(current % m)
        if pisano[len(pisano)-1] == 1 and pisano[len(pisano)-2] == 0:
            break
    return len(pisano) - 2


def get_fib_number(index):

    if index <= 1:
        return index
    prev = 0
    current = 1
    for _ in range(index-1):
        prev, current = current, prev + current
    return current


def get_fibonacci_huge_naive(n, m):

    index = n

    index = index % get_pisano_len(m)
    number = get_fib_number(index)
    answer = number % m
    return answer


if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
