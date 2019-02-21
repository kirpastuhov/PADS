import time


def fib(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, (a+b) % 10
        return b


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
