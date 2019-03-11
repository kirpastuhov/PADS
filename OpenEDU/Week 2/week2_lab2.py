def merge_sort(data):
    if len(data) > 1:
        middle = len(data) // 2
        left = data[:middle]
        right = data[middle:]
        inversion = merge_sort(left) + merge_sort(right)
        l, r = 0, 0
        cursor = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                data[cursor] = left[l]
                l += 1
            else:
                inversion += len(left) - l
                data[cursor] = right[r]
                r += 1
            cursor += 1
        while l < len(left):
            data[cursor] = left[l]
            cursor += 1
            l += 1
        while r < len(right):
            data[cursor] = right[r]
            cursor += 1
            r += 1
        return inversion
    return 0

def read_file():
    with open("input.txt", 'r')as file:
        size = int(file.readline())
        data = [int(num) for num in file.readline().split(" ")]
    return size, data


def main():
    size, data = read_file()
    res = open("output.txt", "w")
    res.write(str(merge_sort(data)))


if __name__ == '__main__':
    main()
