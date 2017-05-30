from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    '''take a message and rotate each character by the integer rot via helper function'''
    newtext = ''
    for char in text:
        newtext += rotate_character(char, rot)
    return newtext


def main():
    '''get message and rotation amount to encrypt from user'''
    from sys import argv, exit

    if not argv[1].isdigit():
        print("Sorry, you did not enter an integer to rotate, try again.")
        exit()
    message = input("Type a message:")
    print(message)
    print(encrypt(message, int(argv[1])))


if __name__ == "__main__":
    main()

