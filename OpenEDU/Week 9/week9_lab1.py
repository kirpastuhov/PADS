import re


def get_indexes(string, sub_string):
    return [m.start(0) + 1 for m in re.finditer('(?='+sub_string+')', string)]


def main():
    with open("input.txt", "r") as file:
        sub_string = file.readline().strip()
        string = file.readline().strip()

    result = get_indexes(string, sub_string)

    with open("output.txt", "w") as res:
        res.write(str(len(result)) + '\n')
        res.write(' '.join(str(r) for r in result))


if __name__ == "__main__":
    main()
