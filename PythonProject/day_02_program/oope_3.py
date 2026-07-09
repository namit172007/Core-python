class Car:
    def __init__(self):
        self.__engine=""
        self._speed=0
        self.company=""
    def engine_setter(self,engine_type):
        self.__engine=engine_type
    def display(self):
        print(f"{self.__engine}::{self._speed}::{self.company}")
c=Car()
c._speed=int(input("ENTER THE SPEED")) # warning
c.company=input("ENTER THE COMPANY")
engine_type=input("ENTER THE TYPE OF ENGINE")
c.engine_setter(engine_type)