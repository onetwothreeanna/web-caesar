def alphabet_position(letter):
    """Receives a letter and returns 0-based numerical
    position of that letter within the alphabet. Disregards case."""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet.find(letter.lower())
    return position

def rotate_character(char, rot):
    """Returns new character - result of rotating char by rot number of places to the right.
    Maintains case, returns nonalphabetic characters unchanged."""

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char not in alphabet:        #if char is not a letter, return unchanged
        return char

    else:            #if char is a letter
        newpos = alphabet_position(char) + rot     #Calculate new index based on rot
        newchar = ""
        if newpos < 26:
            newchar += alphabet[newpos]
        else:
            newchar += alphabet[newpos%26]          #Start back at beginning of alphabet if new index is over 26
        if char == char.upper():                    #If the original letter is uppercase
            return newchar.upper()                  #Mimic case in new character
        else:
            return newchar                  #Otherwise, return in lowercase


def encrypt(text, rot):
    """Returns result of rotating each letter in text by rot places to the right."""
    encrypted = ""
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted
