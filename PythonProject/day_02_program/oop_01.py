class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks = marks
    def display(self):
        print(f"{self.roll_no}::{self.name}::{self.marks}")
    def __str__(self):
        return f"{self.roll_no}::{self.name}::{self.marks}"
    def __del__(self):
        print("OBJECT DESTROYED!!")
s1=Student(13,"namit",238)
s1.display()
print(s1)