text = input("Provide the string: ")
text = text.lower().replace(' ', '').strip()
reversed = text[::-1]

if (text == reversed):
    print("its a palindrome")
else:
    print("it is not a palindrome")