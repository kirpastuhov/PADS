def main():
    results = {}
    with open('input.txt', "r") as file:
        _ = file.readline()
        array = [int(x) for x in file.readline().strip().split(" ")]
        _ = file.readline()
        requests = [int(x) for x in file.readline().strip().split(" ")]
        res = open('output.txt', 'w')
        for i in range(0, len(requests)):
            if requests[i] in results:
                res.write(results[requests[i]] + '\n')
            else:
                binary_search(array, requests[i], results)
                res.write(results[requests[i]] + '\n')


def binary_search(array, value, results):
    l = -1
    r = len(array)
    while (r > l+1 or (r >= len(array) and l < 0 and array[l] != value and array[r] != value)):
        mid = (l+r) / 2
        if array[int(mid)] < value:
            l = mid
        else:
            r = mid

    if r < len(array) and array[int(r)] == value:
        while r < len(array) and array[int(r)] == value:
            r += 1
        while l >= 0 and array[int(l)] == value:
            l -= 1
        l += 2
        results[value] = (f"{int(l)} {int(r)}")

    else:
        results[value] = "-1 -1"


if __name__ == "__main__":
    main()
