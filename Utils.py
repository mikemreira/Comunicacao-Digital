import array


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
