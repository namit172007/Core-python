import math

a = int(input("Enter the number: "))
flag = True

if a > 1:
    if a == 2:
        flag = True
    elif a % 2 == 0:
        flag = False
    else:
        for i in range(3, int(math.sqrt(a)) + 1, 2):
            if a % i == 0:
                flag = False
                break
else:
    flag = False

if flag:
    print("IT IS A PRIME NUMBER")
else:
    print("IT IS NOT A PRIME NUMBER")