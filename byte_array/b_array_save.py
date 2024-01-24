from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

try:
    byte_file = open('file.bin', 'wb')
    byte_file.write(data)
    byte_file.close()

except IOError as e:
    print("I/O error: ", strerror(e.errno))

try:
    byte_file = open('file.bin', 'rb')
    byte_file.readinto(data)
    byte_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error: ", strerror(e.errno))

# Do not use this read unless you 
# are sure it is compatible with bytearray()
try:
    byte_file = open('file.bin', 'rb')
    # you can add int param in read() to read max number of bytes
    read_data = bytearray(byte_file.read())
    byte_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error: ", strerror(e.errno))