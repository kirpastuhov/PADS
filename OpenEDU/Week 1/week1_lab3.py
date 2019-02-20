def insertion(len, data):
    index = []
    for i in range(len):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        index.append(j+2)
    with open("output.txt", "w") as res:
        res.write(' '.join(str(i) for i in index) + '\n')
        res.write(' '.join(str(d) for d in data))


def sum():
    with open('input.txt', "r") as file:
        for number, line in enumerate(file.readlines()):
            if number == 0:
                len = int(line)
                continue
            data = [int(num) for num in line.split(' ')]
    return len, data


if __name__ == "__main__":
    len, data = sum()
    insertion(len, data)
