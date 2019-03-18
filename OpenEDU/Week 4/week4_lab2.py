from collections import deque


def main():
    with open('input.txt', "r") as file:
        commands = int(file.readline())
        queue = deque([])
        res = []
        for i in range(1, commands + 1):
            data = [x for x in file.readline().strip().split(" ")]
            if data[0] == "+":
                queue.append(int(data[1]))
            else:
                res.append(queue.popleft())
    with open("output.txt", "w") as res_file:
        res_file.write('\n'.join(str(d) for d in res))


if __name__ == '__main__':
    main()
