def get_middle_index(index):
    return int((index - 1)/2)


def sum():
    with open('input.txt', "r") as file:
        for number, line in enumerate(file.readlines()):
            if number == 0:
                len = int(line)
                continue
            data = [[i+1, float(num)] for i, num in enumerate(line.split(' '))]
    return len, data


if __name__ == "__main__":
    len, data = sum()
    sorted_data = sorted(data, key=lambda x: x[1])

    min = sorted_data[0][0]
    mid = sorted_data[get_middle_index(len)][0]
    max = sorted_data[-1][0]

with open("output.txt", "w") as res:
    res.write(str(min) + " " + str(mid) + " " + str(max))
