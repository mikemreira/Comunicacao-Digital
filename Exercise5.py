
import random as rand
def binarySymmetricChannel(sequence, expectedBer):
    with open(sequence, 'r', encoding="utf-8") as file:
        char = file.read(1)
        while True:
            num = ord(char)
            print(bin(num).replace('b', '').zfill(8))
            char = file.read(1)
            if not char:
                break

def toBinary(text):
    return ' '.join(format(ord(x), 'b') for x in text)


def BSC(binary, prob):
    print(rand.random())
    interferencia = ""
    print(binary)
    for x in binary:
        print("X => "+x)
        if x == " ":
            interferencia += " "
            continue
        is_wrong = rand.random() < prob
        bit = x
        if is_wrong:
            bit = invertValue(bit)
            interferencia += str(bit)
        else:
            interferencia += str(bit)
    return interferencia

def invertValue(x):
    if x == 1:
        return 0
    return 1

def main():
    binarySymmetricChannel("./TestFilesCD/a.txt", 1)
    file = "hello world"
    print(BSC(toBinary(file), 0.1))
    print(toBinary(file))


if __name__ == "__main__":
    main()
