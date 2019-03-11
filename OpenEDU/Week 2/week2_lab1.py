def read_file():
    with open('input.txt', "r") as file:
        size = int(file.readline())
        data = [int(num) for num in file.readline().split(' ')]
    return size, data


def merge(left, right, left_border, right_border, file):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    file.write(f"{left_border + 1} {right_border + 1} {result[0]} {result[-1]}" + '\n')
    return result


def merge_sort(data, left_border, right_border, file):
    if len(data) == 1:
        return data
    middle = len(data) // 2
    left_data = merge_sort(data[:middle], left_border, left_border + middle - 1, file)
    right_data = merge_sort(data[middle:], left_border + middle, right_border, file)
    return merge(left_data, right_data, left_border, right_border, file)


def main():
    size, data = read_file()
    file = open('output.txt', 'w')
    file.write(" ".join(str(r) for r in merge_sort(data, 0, size - 1, file)))


if __name__ == '__main__':
    main()
