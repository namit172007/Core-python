n=int(input("ENTER THE NUMBER"))
input_list=[]
for i in range (n):
    number=int(input("ENTER THE NUMBER"))
    input_list.append(number)
maximum=float("-inf")
second_maximum=float("-inf")
if input_list[0]>input_list[1]:
    maximum=input_list[0]
    second_maximum=input_list[1]
else:
    maximum = input_list[1]
    second_maximum = input_list[0]
for i in range (2,len(input_list)):
    if input_list[i]>maximum:
        maximum,second_maximum=input_list[i],maximum
    elif input_list[i]>second_maximum:
        second_maximum=input_list[i]
print(f"THE MAXIMUM IS {maximum}")
print(f"THE SECOND MAXIMUM IS {second_maximum}")