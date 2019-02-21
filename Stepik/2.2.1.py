import time
from math import sqrt, pow


def fib(n):
    return int((pow((1+sqrt(5)), n) - pow((1-sqrt(5)), n))/(pow(2, n)*sqrt(5)))


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
