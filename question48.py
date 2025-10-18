class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.width * self.length

rectangle =   Rectangle(5.2, 2) 
print(rectangle.area())