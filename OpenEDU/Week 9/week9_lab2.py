from edx_io import edx_io


def calculate_sum_distance(positions):
    k = len(positions) - 1

    sum = 0
    for p in reversed(positions):
        sum += k * p
        k -= 2

    for i in range(1, len(positions)):
        sum -= i
    return sum


def main():

    mapa = {}
    with edx_io() as io:
        tokens = [t.decode() for t in io.all_tokens()]
        sentence = ''
        for t in tokens:
            sentence += t
        for index, char in enumerate(sentence.replace(" ", "")):
            mapa.setdefault(char, []).append(index)
        sum = 0

        for _, val in mapa.items():
            amount = len(val)
            if amount > 1:
                sum += calculate_sum_distance(val)
        io.write(str(sum))


if __name__ == "__main__":
    main()
