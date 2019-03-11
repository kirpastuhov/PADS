def read_file():
    with open('input.txt', 'r') as file:
        size = int(file.readline())
    return size


def main():
    size = read_file()
    numbers = [i for i in range(1, size + 1)]
    print(numbers)
    for i in range(size):
        if (i > 1):
            numbers[i], numbers[i // 2] = numbers[i // 2], numbers[i]
            print(f'num[i] = {numbers[i]}, num[i // 2] = {numbers[i // 2]}')
    print(numbers)
    return numbers


def write_file(res):
    with open('output.txt', 'w') as file:
        file.write(' '.join(str(r) for r in res))


if __name__ == '__main__':
    write_file(main())

