from edx_io import edx_io


def main():
    with edx_io() as io:
        data = [int(t.decode()) for t in io.all_tokens()]
        N = int(data.pop(0))
        is_heap = True
        for i in range(1, N // 2 + N % 2):
            if (data[i - 1] > data[2 * i - 1] or data[i - 1] > data[2 * i]):
                is_heap = False
                break
        io.write("YES" if is_heap else "NO")

if __name__=="__main__":
    main()
