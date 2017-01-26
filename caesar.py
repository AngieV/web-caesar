def alphabet_position(letter):
    letter = letter.lower()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return alpha.index(letter)

def rotate_character(char, rot):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    encr = (alphabet_position(char) + rot) % 26
    if char.isupper():
        return alpha[encr].upper()
    return alpha[encr]
    
def encrypt(text, rot):
    encrypted = ''
    rot = rot % 26
    for letter in text:
        if letter.isalpha():
            encrypted += rotate_character(letter, rot)
        else:
            encrypted += letter
    return encrypted
