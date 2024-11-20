class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    def bark(self):
        print("Bark")

class Cat(Mammal):
    pass

dog1 = Dog()
# dog1.bark()

# SUPER FUNCTION
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Square(Rectangle):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)
    def area(self):
        return self.length * self.breadth

class Cube(Rectangle):
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
    def volume(self):
        return self.length * self.breadth * self.height

cube = Cube(4, 4, 4)
square = Square(4, 4)
print(cube.volume())
print(square.area())