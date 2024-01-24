from os import strerror

try:
    file = open('newtxt.txt', 'wt')
    for i in range(10):
        line = "line #" + str(i + 1) + "\n"
        for ch in line:
            file.write(ch)
        
    # shortened
    for i in range(10):
        file.write("short line #" + str(i + 1) + "\n")

    file.close()

except IOError as e:
    print("I/O error: ", strerror(e.errno))