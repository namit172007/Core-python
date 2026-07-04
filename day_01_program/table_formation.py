input_string=input("ENTER THE STRING")
input_list=input_string.split(" ")
for exact_string in input_list:
    print(exact_string[::-1],end=" ")
