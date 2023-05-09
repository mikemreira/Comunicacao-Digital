import cv2
import matplotlib.pyplot as mp
import math

from Utils import read_file


def histogram_bmp(file_name):
    image = cv2.imread("./TestFilesCD/lena.bmp")
    vals = image.mean(axis=2).flatten()
    mp.hist(vals, 255)
    mp.xlim([0, 255])
    mp.show()


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


def main():
    percentage_estimate("./ListaPalavrasPT.txt")
    histogram_bmp("lena.bmp")


if __name__ == '__main__':
    main()
