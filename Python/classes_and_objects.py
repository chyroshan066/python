# defining class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

p1 = Point(10, 20)  # creating objects

# p1.x = 20  # creating attributes outside of class
print(p1.x)

# p1.draw()  # accessing class methods

# p2 = Point()
# print(p2.x)