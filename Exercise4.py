

def make_vernam_cypher(plain_text, the_key):
    cipher_text = ""
    for i in range(len(plain_text)):
        char = plain_text[i]
        key_char = the_key[i % len(the_key)]
        cipher_char = chr(ord(char) ^ ord(key_char))
        cipher_text += cipher_char
    return cipher_text


def vernam_decrypt(cipher_text, key):
    plain_text = ""
    for i in range(len(cipher_text)):
        char = cipher_text[i]
        key_char = key[i % len(key)]
        plain_char = chr(ord(char) ^ ord(key_char))
        plain_text += plain_char
    return plain_text


def main_exercise_4():
    file = open("./TestFilesCD/alice29.txt")
    cypher_text = make_vernam_cypher(file.read(), "SECRET")
    plain_text = vernam_decrypt(cypher_text, "SECRET")
    print(cypher_text)
    print(plain_text)


if __name__ == '__main__':
    main_exercise_4()
