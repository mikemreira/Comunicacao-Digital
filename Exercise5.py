import random as rand


def file_in_and_out(sequence, expectedBer):
    with open(sequence, 'r', encoding="utf-8") as file:
        char = file.read(1)
        while True:
            num = ord(char)
            print(bin(num).replace('b', '').zfill(8))
            char = file.read(1)
            if not char:
                break


def to_binary(text):
    return ' '.join(format(ord(x), 'b').zfill(8) for x in text)


def bsc(binary, prob):
    interference = ""
    for x in binary:
        if x == " ":
            interference += " "
            continue
        is_wrong = rand.random() < prob
        bit = x
        if is_wrong:
            bit = invert_value(bit)
        interference += str(bit)
    return interference


def invert_value(x):
    if x == "1":
        return 0
    return 1

def ber_calculator():


def main():
    # binarySymmetricChannel("./TestFilesCD/a.txt", 1)
    file = "hello world"
    print("Original value in bits " + to_binary(file))
    print("New value in bits  ->  " + bsc(to_binary(file), 0.5))


if __name__ == "__main__":
    main()
