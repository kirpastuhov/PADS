with open('input.txt', "r") as file:
    _ = int(file.readline())
    data = [int(num) for num in file.readline().split(' ')]
with open("output.txt", "w") as res:
    for i in range(len(data)):
        minimal = min(data[i:])
        index = data[i:].index(minimal) + i
        if minimal < data[i]:
            data[i], data[index] = minimal, data[i]
            res.write(f'Swap elements at indices {i+1} and {index+1}.\n')

    res.write("No more swaps needed.\n")
    res.write(' '.join(str(d) for d in data))
