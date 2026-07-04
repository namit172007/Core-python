import math
def angstrom_check(a):
    temp=a
    digit_count=len(str(a))
    checknum=0
    while (a>0):
        dig=a%10
        a=a//10
        checknum+=math.pow(dig,digit_count)
    return checknum==temp
n=int(input("ENTER THE NUMBER"))
decision=angstrom_check(n)
if decision:
    print("IT IS AN ANGSTROM NUMBER")
else:
    print("IT IS NOT AN ANGSTROM NUMBER")
