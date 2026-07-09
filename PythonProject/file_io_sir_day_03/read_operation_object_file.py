import pickle
# from write_operation_object_file import Employee

with open('../files/employee.txt', 'rb') as file:
    obj = pickle.load(file)
    print("Printing Employee information after unpickling")
    obj.display()