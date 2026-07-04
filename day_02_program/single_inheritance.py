class Vehicle:
    def __init__(self,color,company):
        self.color=color
        self.company=company
class Bike(Vehicle):
    def __init__(self,color,company,engine_cc):
        super().__init__(color,company)
        self.engine_cc=engine_cc
    def get_value(self):
        print(f"{self.color}::{self.company}::{self.engine_cc}")
color=input("ENTER COLOUR")
company=input("ENTER COMPANY")
engine=int(input("ENTER THE ENGINE CC"))
b=Bike(color,company,engine)
b.get_value()


