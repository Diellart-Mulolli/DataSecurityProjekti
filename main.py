import string 

def denumerate(indices):
    alphabet = string.ascii_uppercase
    return [alphabet[i] for i in indices]

def decharrify(chars):
    return "".join(chars)
