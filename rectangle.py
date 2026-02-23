class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r1 = Rectangle(50, 20)
print("Area:", r1.area())