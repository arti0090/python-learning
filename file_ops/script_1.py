try:
    stream = open("./file.txt", "rt")
    stream.close()
except Exception as e:
    print("Cant open the file", e, ", creating one")
    stream = open("./file.txt", "x")
    stream.close()
    
# using OS system stream errors
from os import strerror

try:
    stream = open("./file.txt", "rt")
    stream.close()
except Exception as e:
    print("Cant open the file", strerror(e.errno))
