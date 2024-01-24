from os import strerror

src = input("Input sourcefile: ")
try:
    src_file = open(src, 'rb')
except IOError as e:
    print("Unable to open source file: ", strerror(e.errno))
    exit(e.errno)

dst = input("Input name of target: ")
try:
    dst_file = open(dst, 'wb')

except IOError as e:
    print("Unable to create destination file: ", strerror(e.errno))
    exit(e.errno)

buffer = bytearray(65536)
sum = 0

try:
    read = src_file.readinto(buffer)
    
    while read > 0:
        saved = dst_file.write(buffer[:read])
        sum += saved
        read = src_file.readinto(buffer)

except IOError as e:
    print("Unable to create destination file: ", strerror(e.errno))
    exit(e.errno)

print(sum,'bytes writen correctly')
src_file.close()
dst_file.close()