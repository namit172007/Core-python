class Shape:
    def area(self):
        print('Shape Area Method')


class Rectangle(Shape):
    def area(self):
        print('Rectangle Area Method')


r = Rectangle()
r.area()
# ________________________________________________
s = Shape()
s.area()
# _________________________________________________
shape: Shape = Rectangle()
shape.area()
