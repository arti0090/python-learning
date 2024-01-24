text = input("input first value: ").strip()
tested = input("input second value: ").strip()

if len(text) != len(tested):
    print("Words cannot be anagrams due to different lenght.")
    import sys
    sys.exit()

text = list(text.lower().strip(""))
tested = list(tested.lower().strip(""))

iter_test = text.copy()

for char in iter_test:
    if char in tested:
        text.remove(char)
        tested.remove(char)

if text == [] and tested == []:
    print("Words are anagrams.")
else:
    print("Words are not anagrams.")
