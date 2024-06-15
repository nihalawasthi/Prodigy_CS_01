# Caesar Cipher

def encrypt():
    text = input("enter text : ")
    shift = input("enter shift : ")
    etext = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                etext += chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
            else:
                etext += chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
        else:
            etext += char
    return etext

def decrypt():
    etext = input("enter etext : ")
    shift = input("enter shift : ")
    decrypted_text = ""
    for char in etext:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A' ) - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a' ) - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text

while True:
    encrypt()
    decrypt()
