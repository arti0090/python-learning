class Stack:
    def __init__(self):
        # __var makes variable private
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        val = self.__stack[-1]
        del self.__stack[-1]
        return val

# additional class
class StackSum(Stack):
    def __init__(self):
        # In Python class HAS TO BE inited
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum

stack_obj = StackSum()

stack_obj.push(3)
stack_obj.push(2)
stack_obj.push(1)

print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())

# ----------- after StackSum ---------- #

for i in range(5):
    stack_obj.push(i)
print(stack_obj.get_sum())

for i in range(5):
    print(stack_obj.pop())