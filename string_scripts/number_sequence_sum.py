import sys

seq = input("Input sequence of numbers spaced with (space): ")
strings = seq.split()
if len(strings) == 0:
    print("Sequnce is empty, exiting")
    sys.exit()
total = 0

try:
    for subseq_number in strings:
        total += float(subseq_number)
    print("Sum of numbers: ", total)
except:
    print(subseq_number, " is not a number.")