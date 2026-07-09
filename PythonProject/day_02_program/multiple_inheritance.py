class Calculator:
    def add(self, a, b):
        print("Addition :", a + b)
class ScientificCalculator:
    def square(self, n):
        print("Square :", n * n)
class SmartCalculator(Calculator, ScientificCalculator):
    def cube(self, n):
        print("Cube :", n * n * n)
s = SmartCalculator()

s.add(10, 20)
s.square(5)
s.cube(3)