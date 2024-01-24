iban = input("Provide the IBAN number: ")
iban = iban.replace(' ', '')

if not iban.isalnum():
    print("Incorrect chars provided.")
elif len(iban) < 15:
    print("IBAN provided is too short.")
elif len(iban) > 31:
    print("IBAN provided is too long.")

iban = (iban[4:] + iban[0:4]).upper()
iban_char = ''

for char in iban:
    if char.isalpha():
        iban_char += str(10 + ord(char) - ord('A'))
    else:
        iban_char += char

ibann = int(iban_char)
if ibann % 97 == 1:
    print('IBAN OK')
else:
    print("IBAN incorrect")
