def binarySymmetricChannel(sequence, expectedBer):
    with open(sequence, 'r', encoding="utf-8") as file:
        char = file.read(1)
        while True:
            num = ord(char)
            print(bin(num).replace('b', '').zfill(8))
            char = file.read(1)
            if not char:
                break


def main():
    binarySymmetricChannel("./TestFilesCD/a.txt", 1)


if __name__ == "__main__":
    main()
