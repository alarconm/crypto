from helpers import alphabet_position, rotate_character

def encrypt(message, key):
    '''return message with each character rotated by the difference
    between the letter and message and letter in the key'''
    keylist = []
    newmessage = ''

    for char in key:    #put key characters into a new list
        keylist.append(alphabet_position(char))
    keyaccum = 0
    for char in message:
        if not char.isalpha(): # keep any non-alpha characters intact
            newmessage += char
        else: #rotate the character by the key
            newmessage += rotate_character(char, keylist[keyaccum % len(key)])
            keyaccum += 1 #add one so that next letter in key is used next iteration
    return newmessage


def main():
    '''get message and ecryption key from user, start program'''
    from sys import argv, exit
    for char in argv[1]: #exit program if any characters aren't alpha
        if not char.isalpha():
            print("usage: python vigenere.py keyword\n -keyword : The string "
                  "to be used as a 'key' to encrypt your message. Should only contain "
                  "alphabetic characters-- no numbers or special characters.")
            exit()
    message = input("Type a message:")
    print(message)
    key = argv[1] #key is entered when program is run from the command line
    print(encrypt(message, key))


if __name__ == "__main__":
    main()
