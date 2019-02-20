from decimal import Decimal


def sum():
    with open('input.txt', "r") as file:
        a = file.readline()
        b = a.split(" ")
        dec_a = Decimal(b[0])
        dec_b = Decimal(b[1]).__pow__(2)
        sum = dec_a + dec_b
    with open("output.txt", "w") as res:
        res.write(str(int(sum)))


if __name__ == "__main__":
    sum()
