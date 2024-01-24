from os import strerror

# src = input("Input sourcefile: ")
src = 'sample_1.txt'
try:
    src_file = open(src, 'rt')
except IOError as e:
    print("Unable to open source file: ", strerror(e.errno))
    exit(e.errno)

letters = dict()

for line in src_file.readline():
    for ch in line:
        ch = ch.lower()
        if ch in letters:
            letters[ch] = letters[ch] + 1
        else:
            letters[ch] = 1

src_file.close()

for k,v in letters.items():
    print(str(k) + ' -> ' + str(v))