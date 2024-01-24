text = input("Insert message: ")
while True:
    try:
        shift = int(input("Insert cipher shift: "))
        if shift < 1 or shift > 25:
            print("Provided number is not in range of 1..25, try again.")
            continue
        break
    except ValueError:
        print("Provided data is not integer number, try again.")
        

cipher = ''

for char in text:
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        code = ((ord(char) + shift))
        if code > ord('Z'):
            code = code - ord('Z') + (ord('A') - 1)
        cipher += chr(code)
    elif ord(char) >= ord('a') and ord(char) <= ord('z'):
        code = ((ord(char) + shift))
        if code > ord('z'):
            code = code - ord('z') + (ord('a') - 1)
        cipher += chr(code)
    else:
        cipher += char

print(cipher)
