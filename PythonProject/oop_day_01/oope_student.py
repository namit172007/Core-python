# Create a class named Student.
# Instance Variables
# roll_no
# name
# marks
# Methods
# set_details()
# Stores roll number, name, and marks.
# display_details()
# Displays all student details neatly.
# is_pass()
# Returns True if marks are 35 or above, otherwise False.
from tarfile import TruncatedHeaderError


class Student :
    def set_details(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
    def display_details(self):
        print(f"{self.name}\t{self.roll_no}\t{self.marks}")
    def is_pass(self):
        return self.marks>=35
s=Student()
roll_no=int(input("ENTER TEH ROLL NO"))
name=input("ENTER THE NAME")
marks=int(input("ENTER THE MARKS"))
s.set_details(roll_no,name,marks)
s.display_details()
if s.is_pass():
    print("STATUS :: PASS")
else:
    print("STATUS :: FAIL")
