from os import strerror

try:
    line_counter = char_counter = 0
    stream = open("text.txt", "rt")
    line = stream.readline()
    
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            char_counter += 1
        
        line = stream.readline()
    
    stream.close()
    
    print("\n\n")
    print("Lines in file:", char_counter)
    print("Chars in file:", line_counter)
except IOError as e:
    print("I/O Error: ", strerror(e.errno))