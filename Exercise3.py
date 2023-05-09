import math
import os
import random
import string


def symbol_generator(symbols, size, file_name, probabilities=None):
    if probabilities is None:
        output_array = random.choices(symbols, k=size)
    else:
        output_array = random.choices(symbols, probabilities, k=size)
    f = open(file_name, "w")
    f.write(" ".join(output_array))
    f.close()
    f = open(file_name, "r")
    return f.read()


def entropy_compare(sizeM, sizeN):
    symbols = ['a', 'b', 'c', 'd', 'e', 'f']
    probabilities = [0.9, 0.1, 0, 0, 0, 0]
    result1 = symbol_generator(symbols, sizeM, "entropyCompare1", probabilities).split(" ")
    result2 = symbol_generator(symbols, sizeN, "entropyCompare2", probabilities).split(" ")
    entropy1 = entropy_calculator(symbols, result1)
    entropy2 = entropy_calculator(symbols, result2)
    return entropy1, entropy2


def entropy_calculator(symbols, text):
    entropy = 0.0
    for i in range(0, len(symbols)):
        px = text.count(symbols[i]) / len(text)
        if px == 0:
            continue
        entropy -= (math.log(px, 2) * px)
    return entropy


def password_generator():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password_length = random.randint(8, 12)
    return symbol_generator(alphabet, password_length, "passwords")


def main_exercise_3():
    fmp = [0.9, 0.1, 0, 0, 0, 0]
    m = ['a', 'b', 'c', 'd', 'e', 'f']
    file_name = "symbolGenerator"
    print("result from generating symbols")
    print(symbol_generator(m, 20, file_name, fmp))
    open(file_name, "w").close()
    # comment this vvv if you want file to appear
    os.remove(file_name)
    print()
    print("Entropy with size 20 and size 10000000 respectfully")
    print(entropy_compare(20, 10000000))
    print()
    print("spaces for better look")
    for i in range(5):
        print(password_generator())


if __name__ == '__main__':
    main_exercise_3()
    # entropy_compare(20, 30)
