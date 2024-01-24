from os import strerror

try:
    char_count = line_count = 0
    
    for line in open('text.txt', 'rt'):
        line_count += 1
        for char in line:
            print(char, end='')
            char_count += 1

    print("\n\n")
    print("Chars in file: ", char_count)
    print("Lines in file: ", line_count)    

except IOError as e:
    print("I/O error: ", strerror(e.errno))