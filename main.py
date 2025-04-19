import string 

def uppercased(text):
    return text.upper()

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

# main function
# This function takes a plaintext and a key, resizes the key, and then encodes the plaintext
# using the coded function. It returns the encoded text as a string.

def coded(text, key):
    n = len(string.ascii_uppercase)
    return [(2 * n - text[i] - key[i] - 1) % n for i in range(len(text))]

# Main Program Entrance 
def main():
    print("Beaufort Cipher")
    while True:
        action = input("\nE/e for Encoding | D/d for Decoding | O/o for Exit | Enter command: ").strip().lower()
        if action in ['e','d']:
            input_text = uppercased(input("Enter text:").strip())
            textArr = charrify(input_text)  # charrify function will be defined later
            if not textArr:
                print("ERROR: Invalid characters in text. Use only letters.")
                continue
            textIntArr = enumerate_chars(textArr) #enumerate_chars function also will be completed later by the colleague
            input_key = uppercased(input("Enter key:").strip())
            keyArr = charrify(input_key)

