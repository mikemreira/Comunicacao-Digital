def makeVernamCypher(plainText, theKey):
    cipher_text = ""
    for i in range(len(plainText)):
        char = plainText[i]
        key_char = theKey[i % len(theKey)]
        cipher_char = chr(ord(char) ^ ord(key_char))
        cipher_text += cipher_char
    return cipher_text


def main_exercise_4():
    file = open("./TestFilesCD/alice29.txt")
    cypher_text = makeVernamCypher(file.read(), "SECRET")
    plain_text = makeVernamCypher(cypher_text, "SECRET")
    print(cypher_text)
    print(plain_text)


if __name__ == '__main__':
    main_exercise_4()
