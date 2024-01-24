from os import strerror

# src = input("Input sourcefile: ")
src = 'sample_2.txt'
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

letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))

for k,v in letters.items():
    print(str(k) + ' -> ' + str(v))

try:
    dst_file = open(src.split('.')[0] + '.hist', 'wt')
    for k,v in letters.items():
        dst_file.write(str(k) + ' -> ' + str(v) + "\n")
    dst_file.close()

except IOError as e:
    print("I/O error: ", strerror(e.errno))