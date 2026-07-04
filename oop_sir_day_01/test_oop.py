class Person:
    first_name = 'Namit'
    last_name = 'Rathi'

    @staticmethod
    def get_address():
        address = 'Indore'
        return address

    @classmethod
    def get_first_name(cls):
        return cls.first_name

print(Person.first_name)
print(Person.last_name)
print(Person.get_address())
print(Person.get_first_name())
p = Person()
print(p.get_first_name())
