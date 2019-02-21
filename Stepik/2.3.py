from fractions import gcd


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))  # standard library


if __name__ == "__main__":
    main()
