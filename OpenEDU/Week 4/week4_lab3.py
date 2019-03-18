def main():
    with open('input.txt', "r") as file:
        commands = int(file.readline())
        res = []
        for i in range(1, commands + 1):
            data = file.readline().strip()
            res.append(check_brackets(data))
    with open("output.txt", "w") as res_file:
        for i in res:
            res_file.write("YES\n" if i else "NO\n")


def check_brackets(text):
    opening = "(["
    closing = ")]"
    stack = []
    for character in text:
        if character in opening:
            stack.append(opening.index(character))
        elif character in closing:
            if stack and stack[-1] == closing.index(character):
                stack.pop()
            else:
                return False

    return (not stack)


if __name__ == '__main__':
    main()
