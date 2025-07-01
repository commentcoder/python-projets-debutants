def caesar_cipher(message, shift=3, decode=False):
    if decode:
        shift = -shift

    result = ""

    for letter in message.upper():
        if letter.isalpha():
            ascii_value = ord(letter) - ord("A")
            shifted_value = (ascii_value + shift) % 26
            result += chr(shifted_value + ord("A"))
        else:
            result += letter

    return result


def main():
    message = input("Que est votre message : ")

    encoded = caesar_cipher(message)
    decoded = caesar_cipher(encoded, decode=True)

    print("encoded =", encoded, "decoded =", decoded)


if __name__ == "__main__":
    main()
