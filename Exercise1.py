import array


def geometric_progression(n, u, r):
    arr = array.array("f", (0 for _ in range(0, n)))
    for i in range(0, n):
        arr[i] = (u * r) ** i
    return arr


def mdc(a, b):
    while b != 0:
        (b, a) = (a % b, b)
    return a

