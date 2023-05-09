import array
import cv2
import collections
import matplotlib.pyplot as mp
import numpy as np
import math


def read_file(file_name):
    arr = array.array("i", (0 for _ in range(0, 255)))
    f = open(file_name, "r", encoding="ISO-8859-1")
    text = f.read()
    for i in range(0, len(text)):
        try:
            arr[ord(text[i])] += 1
        except IndexError:
            continue
    f.close()
    return arr, text


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


def histogram_bmp(file_name):
    image = cv2.imread("./TestFilesCD/lena.bmp")
    vals = image.mean(axis=2).flatten()
    mp.hist(vals, 255)
    mp.xlim([0, 255])
    mp.show()


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
        print("Informaçao propria de", list(letters_hist.keys())[i], "=", ip*-1)
    print("Entropia =", abs(sum(entropy)))


def percentage_estimate(file_name):
    arr, text = read_file(file_name)
    entropy = 0
    filtered_arr = list(filter(lambda frequency: frequency > 0, arr))
    for i in range(0, len(arr)):
        if arr[i] != 0:
            print(chr(i), " = ", (arr[i] / len(text)) * 100, "%")
        else:
            continue
    for i in range(0, len(filtered_arr)):
        px = filtered_arr[i] / len(text)
        entropy -= (math.log(px, 2) * px)
    print("Entropia ficheiro = ", entropy)

