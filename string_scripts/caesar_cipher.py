def decrypt(cipher = ''):
    if cipher == '':
        cipher = input("Write ciphered message: ")
    text = ''
    for char in cipher:
        if not char.isalpha():
            text += char
            continue
        char = char.upper()
        code = ord(char) - 1

        if code < ord('A'):
            code = ord('Z')

        text += chr(code)

    return text

def encrypt(text = ''):
    if text == '':
        text = input("Insert message: ")
    cipher = ''
    for char in text:
        if not char.isalpha():
            cipher += char
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)
    
    return cipher

message = encrypt("dupsko sto")
print(message)
print(decrypt(message))