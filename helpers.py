def alphabet_position(letter):
    '''take a letter and return its index in the alphabet'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    return alphabet.find(letter)


def rotate_character(char, rot):
    '''receive a character and integer, rotate that character by the
    integer and return new letter'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha() == False:
        return char
    else:
        newchar = alphabet[(alphabet_position(char) + rot) % 26]
        if char.isupper():
            return newchar.upper()
        else:
            return newchar