class Laptop:
    def __init__(self,brand="hp",ram=16,ssd=512):
        self.brand=brand
        self.ram=ram
        self.ssd = ssd
    def display(self):
        print(f"{self.brand}::{self.ram}::{self.ssd}")
l1=Laptop()
l1.display()
l2=Laptop("HP")
l2.display()
l3=Laptop("Lenovo",16,512)
l3.display()