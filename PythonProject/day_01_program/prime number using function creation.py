import math

def prime_number (a):
    if a > 1:
        if a == 2:
            return True
        elif a % 2 == 0:
            return False
        else:
            for i in range(3, int(math.sqrt(a)) + 1, 2):
                if a % i == 0:
                    return False
    return True

n = int(input("Enter the number: "))
decision=prime_number(n)
if decision:
    print("IT IS A PRIME NUMBER")
else:
    print("IT IS NOT A PRIME NUMBER")
