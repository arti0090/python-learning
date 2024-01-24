# class implemented fibonacci generator
class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("__iter__")		
		return self

	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret


# yield-ed fibonacci generator
def Fibb(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n


for i in Fib(10):
	print(i)

fibs = list(Fibb(10))
print(fibs)