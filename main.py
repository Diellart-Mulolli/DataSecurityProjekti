import string 

def denumerate(indices):
    alphabet = string.ascii_uppercase
    return [alphabet[i] for i in indices]

def decharrify(chars):
    return "".join(chars)

# key resize function
# This function resizes the key to match the size of the plaintext or ciphertext
# by repeating the key as many times as necessary and then slicing it to the correct size.
# TEXTINPUT
# KEYKEYLEY

def key_resize(key, size):
    return (key * (size // len(key) + 1))[:size]