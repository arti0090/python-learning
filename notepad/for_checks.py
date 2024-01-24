class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"
