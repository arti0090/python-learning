two = lambda : 2
square = lambda x : x * x
power = lambda x, y : x ** y

for a in range(-2, 3):
    print(square(a), end = ' ')
    print(power(a, two()))

# -------------- #
# lambda in maps #
lista_1 = [x for x in range(5)]
lista_2 = list(map(lambda x: 2 ** x, lista_1))
print(lista_2)

for x in map(lambda x: x * x, lista_2):
	print(x, end=' ')
print()

# -------------- #
# filter in maps #

from random import seed, randint

seed()
dane = [randint(-10,10) for x in range(5)]
filtr = list(filter(lambda x: x > 0 and x % 2 == 0, dane))

print(dane)
print(filtr)