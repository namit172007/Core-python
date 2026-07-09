n=int(input("ENTER THE NUMBER"))
temp=n
rev=0
while(n>0):
    dig=n%10
    n=n/10
    rev=rev*10+dig
if (rev==temp):
    print("IT IS A PALINDROME NUMBER")
else :
    print("IT IS NOT A PALINDROME NUMBER")