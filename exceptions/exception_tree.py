def show_tree(exceptionClass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(exceptionClass.__name__)

    for subclass in exceptionClass.__subclasses__():
        show_tree(subclass, nest + 1)

show_tree(BaseException)