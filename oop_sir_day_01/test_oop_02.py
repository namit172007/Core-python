class Person:

    def __init__(self):
        self.first_name = 'Namit'
        self.last_name = 'Rathi'

    def get_address(self):
        self.address = 'Indore'
        return self.address


p = Person()
print(p.first_name)
print(p.last_name)
print(p.get_address())
print(p.address)
