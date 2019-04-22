def main():
    with open("input.txt", "r") as file:
        text = [float(x) for x in file.readline().strip().split(" ")]
        print(text)
        n = text[0]
        a = text[1]

        print(find_min_height(n, 0, a))
        with open("output.txt", "w") as res_file:
            res_file.write(str(find_min_height(n, 0, a)))


def find_min_height(n, left, right):
    last = -1
    left_height = right

    while ((right-left) > 0.00000000001):
        mid = (left+right) / 2
        prev = left_height
        current = mid
        above_ground = current > 0
        for i in range(3, int(n)+1):
            next = 2 * current - prev + 2
            above_ground &= next > 0
            prev = current
            current = next

        if above_ground:
            right = mid
            last = current
        else:
            left = mid
    return last


if __name__ == "__main__":
    main()
