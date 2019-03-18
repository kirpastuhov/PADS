def main():
    with open('input.txt', "r") as file:
        commands = int(file.readline())
        stack = []
        res = []
        for i in range(1, commands + 1):
            data = [x for x in file.readline().strip().split(" ")]
            if data[0] == "+":
                stack.append(int(data[1]))
            else:
                res.append(stack.pop())
    with open("output.txt", "w") as res_file:
        res_file.write('\n'.join(str(d) for d in res))


if __name__ == '__main__':
    main()
