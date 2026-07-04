class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print(f"EMPLOYEE ID : {self.emp_id}")
        print(f"NAME        : {self.name}")
        print(f"SALARY      : {self.salary}")
class Manager(Employee):
    def __init__(self,emp_id,name,salary,department):
        super().__init__(emp_id,name,salary)
        self.department=department
    # def display_manager(self):
    #     self.display()
    #     print(f"DEPARTMENT  : {self.department}")
    def display(self):
        super().display()
        print(f"DEPARTMENT : {self.department}")
emp_id=int(input("ENTER THE EMPLOYEE_ID"))
name=input("ENTER THE NAME")
salary=int(input("ENTER THE SALARY"))
department=input("ENTER THE DEPARTMENT NAME")
e1=Manager(emp_id,name,salary,department)
e1.display()
