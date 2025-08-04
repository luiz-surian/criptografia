def shift_character(c, shift):
    # The case if the letter is in lowercase
    if (c >= 'a' and c <= 'z'):
        shifted_character = chr((ord(c) + shift - ord('a')) % 26 + ord('a'))
    # The case if the letter is in uppercase
    elif (c >= 'A' and c <= 'Z'):
        shifted_character = chr((ord(c) + shift - ord('A')) % 26 + ord('A'))
    # If the character is not an alphabet
    else:
        shifted_character = c

    return shifted_character


def cesar_encrypt(str, n=0):
    response = ""
    for c in str:
        response += shift_character(c, n)
    return response


def cesar_decrypt(str, n=0):
    response = cesar_encrypt(str, -n)
    return response
