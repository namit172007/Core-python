# Create a class named Rectangle.
#
# Instance Variables
# length
# breadth
# Methods
# set_dimensions(length, breadth)
# Store the dimensions.
# area()
# Return the area.
# perimeter()
# Return the perimeter.
# is_square()
# Return True if the rectangle is actually a square, otherwise False.
# resize(increase_length, increase_breadth)
# Increase the current dimensions by the given values.
class Rectangle:
    def set_dimensions(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        compute_area=self.l*self.b
        return compute_area
    def perimeter(self):
        compute_perimeter=2*(self.l+self.b)
        return compute_perimeter
    def is_sqaure(self):
        return self.l==self.b
    def resize(self,delta_l,delta_b):
        self.l+=delta_l
        self.b+=delta_b
r=Rectangle()
l=int(input("ENTER THE LENGTH"))
b=int(input("ENTER THE BREADTH"))
r.set_dimensions(l,b)
option=int(input("ENTER THE DIFFERENT CHOICES TO PERFORM THE DIFFERENT OPERATIONS \n1.AREA\n2.PERIMETER\n3.IS SQUARE\n4.RESIZE\n0.EXIT\nENTER YOUR CHOICE"))
while(option!=0):
    if option==1:
        print(f"THE AREA IS {r.area()}")
    elif option==2:
        print(f"THE PERIMETER IS {r.perimeter()}")
    elif option==3:
        if r.is_sqaure():
            print("IS SQUARE")
        else:
            print("IS RECTANGLE")
    elif option==4:
        delta_l=int(input("ENTER THE CHANGE IN THE LENGTH"))
        delta_b=int(input("ENTER THE CHANGE IN THE BREADTH"))
        r.resize(delta_l,delta_b)
    option=int(input("ENTER YOUR CHOICE"))