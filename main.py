import Exercise1 as ex1
import Exercise2 as ex2
import Exercise3 as ex3

def main():
    print(ex1.mdc(1000, 300))
    print(ex1.mdc(1800, 1500))
    print(ex1.mdc(1800, 1050))
    arr = ex1.geometric_progression(10, 1, 2)
    for i in range(0, len(arr)):
        print(i + 1, " -> ", arr[i])
    ex2.most_less_frequent("./TestFilesCD/alice29.txt")

    # Exercise 2 tests
    ex2.histogram("./TestFilesCD/alice29.txt")
    ex2.percentage_estimate("./ListaPalavrasPT.txt")
    ex2.histogram_bmp("lena.bmp")

    # Exercise 3 tests
    # Exercise 4 tests
    # Exercise 5 tests


if __name__ == '__main__':
    main()
