import array
import math

import numpy as np
import collections
import matplotlib.pyplot as mp
from Utils import read_file


def geometric_progression(n, u, r):
    arr = array.array("f", (0 for _ in range(0, n)))
    for i in range(0, n):
        arr[i] = (u * r) ** i
    return arr


def mdc(a, b):
    while b != 0:
        (b, a) = (a % b, b)
    return a


def most_less_frequent(file_name):
    arr, _ = read_file(file_name)
    filtered_arr = list(filter(lambda frequency: frequency > 0, arr))
    max_int = max(filtered_arr)
    min_int = min(filtered_arr)
    max_char = chr(arr.index(max_int))
    min_char = chr(arr.index(min_int))
    print("Min frequency =", min_int)
    print("Min character =", min_char)
    print("Max frequency =", max_int)
    print("Max character =", max_char)


def histogram(file_name):
    file = open(file_name, "r", encoding="ISO-8859-1")
    text = file.read()
    letters_hist = collections.Counter(text.replace('\n', ''))
    file.close()
    counts = letters_hist.values()
    letters = sorted(letters_hist.keys())
    bar_x_locations = np.arange(len(counts))
    mp.title = "Ocorrências de caracteres"
    mp.xlabel = "Caracteres"
    mp.ylabel = "Ocorrências"
    mp.bar(bar_x_locations, counts, align='center', data="Ocorrências")
    mp.xticks(bar_x_locations, letters)
    mp.show()
    entropy = array.array("f", (0 for _ in range(0, len(letters_hist.values()))))
    total = sum(letters_hist.values())
    for i in range(0, len(letters)):
        ip = math.log(list(letters_hist.values())[i] / total, 2)
        entropy[i] = ip * (list(letters_hist.values())[i] / total)
        print("Informaçao propria de", list(letters_hist.keys())[i], "=", ip * -1)
    print("Entropia =", abs(sum(entropy)))


def main():
    print(mdc(1000, 300))
    print(mdc(1800, 1500))
    print(mdc(1800, 1050))
    arr = geometric_progression(10, 1, 2)
    for i in range(0, len(arr)):
        print(i + 1, " -> ", arr[i])
    most_less_frequent("./TestFilesCD/alice29.txt")
    histogram("./TestFilesCD/alice29.txt")


if __name__ == '__main__':
    main()