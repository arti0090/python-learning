class PizzaError(Exception):
    def __init__(self, pizza = 'unknown', message = ''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza = 'unknown', cheese = '> 100', message = ''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def makePizza(pizza, cheese):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "brak wybranej pizzy w menu")
	if cheese > 100:
		raise TooMuchCheeseError(pizza, cheese, "za duzo sera")
	print("Pizza gotowa!")

for (pizza, cheese) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pizza, cheese)
	except TooMuchCheeseError as tmce:
		print(tmce, ':', tmce.cheese)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)
