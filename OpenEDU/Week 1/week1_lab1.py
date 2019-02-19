def sum():
    with open('input.txt', "r") as file:
        a = file.readline()
        b = a.split(" ")
        sum = int(b[0]) + int(b[1])
    with open("output.txt", "w") as res:
        res.write(str(sum))


if __name__ == "__main__":
    sum()
