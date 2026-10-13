class Rectangle:
    def __init__ (self , width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.width+self.height)

    def __str__(self):
        return f"({self.width} x {self.height})"

r = Rectangle(3,9)

print(r,r.area(),r.perimeter())

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)

#     def __str__(self):
#         return f"Rectangle({self.width} x {self.height})"

# r = Rectangle(3, 4)
# print(r, r.area(), r.perimeter())    # Rectangle(3 x 4) 12 14
