import random
LENGTH = 10000


def creating_arrays(n):
    a = [0] * LENGTH
    c = [[0]] * n
    for i in range(0, LENGTH):
        a[i] = i
    random.shuffle(a)
    serial_number = 1
    for i in range(n):
        b = [random.randint(0, 10000) for i in range(a[i])]
        if serial_number % 2 == 0:
            c[i] = sorted(b)
        else:
            c[i] = sorted(b, reverse=True)
        serial_number += 1
    return c


d = int(input("enter number of array :"))
print(creating_arrays(d))
