import string
import queue
from edx_io import edx_io

registers = {}
queue = queue.Queue()
labels = {}
p = 0
q = False


def put(v):
    queue.put(v % 65536, False)


def get():
    return queue.get(False)


def jump(lbl):
    global p
    p = labels[lbl]


def execute(cmd, io):
    c = cmd[0]
    if c == '+':
        put(get() + get())
    elif c == '-':
        a = get()
        put(a - get())
    elif c == '*':
        put(get() * get())
    elif c == '/':
        a = get()
        b = get()
        put(0 if b == 0 else a // b)
    elif c == '%':
        a = get()
        b = get()
        put(0 if b == 0 else a % b)
    elif c == '>':
        registers[cmd[1]] = get()
    elif c == '<':
        put(registers[cmd[1]])
    elif c == 'P':
        if len(cmd) == 1:
            io.writeln(get())
        else:
            io.writeln(registers[cmd[1]])
    elif c == 'C':
        if len(cmd) == 1:
            io.write(chr(get() % 256))
        else:
            io.write(chr(registers[cmd[1]] % 256))
    elif c == ':':
        labels[cmd[1:]] = p
    elif c == 'J':
        jump(cmd[1:])
    elif c == 'Z':
        if registers[cmd[1]] == 0:
            jump(cmd[2:])
    elif c == 'E':
        if registers[cmd[1]] == registers[cmd[2]]:
            jump(cmd[3:])
    elif c == 'G':
        if registers[cmd[1]] > registers[cmd[2]]:
            jump(cmd[3:])
    elif c == 'Q':
        global q
        q = True
    else:
        put(int(cmd))


with edx_io() as io:
    tokens = [t.decode() for t in io.all_tokens()]
    print(tokens)
    labels = {label[1:]: i for i, label in enumerate(tokens) if label[0] == ':'}
    print(labels)
    registers = dict.fromkeys(string.ascii_lowercase, 0)

    print(registers)
    lt = len(tokens)

    while p < lt and not q:
        execute(tokens[p], io)
        p += 1
