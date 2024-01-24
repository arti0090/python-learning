import time
string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
        time.sleep(0.2)
except MemoryError:
    print('To nie jest smieszne!')