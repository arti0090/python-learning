def fun(n): 
    for i in range(n): 
        yield i 

def square_number_gen(n):
    square = 1
    for i in range(n):
        yield square
        square *= 2

for v in fun(5): 
    print(v)

for v in square_number_gen(8):
    print(v)

t = [x for x in square_number_gen(5)]
print(t)