import random


def quick_sort(nums, fst, lst, k):
    if fst >= lst:
        return

    i, j = fst, lst
    x = nums[(lst - fst) // 2]
    print(nums)
    print(x)
    while i <= j:
        while nums[i] < x:
            i += k
        while nums[j] > x:
            j -= k
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + k, j - k
    quick_sort(nums, fst, j, k)
    quick_sort(nums, i, lst, k)


def read_file():
    with open('input.txt', "r") as file:
        size = [int(s) for s in file.readline().split(' ')]
        data = [int(num) for num in file.readline().split(' ')]
    return size, data


size, data = read_file()
n = size[0]
k = size[1]

offset = n - n % k
for i in range(k):
    index = i + offset
    quick_sort(data, i, index if index < n else index - k, k)

result = True

for i in range(n-1):
    if data[i] > data[i+1]:
        result = False
        break
with open("output.txt", "w") as res:
    res.write("YES" if result else "NO")
