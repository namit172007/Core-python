# 1. Display Book 1
#
# 2. Display Book 2
#
# 3. Issue Book 1
#
# 4. Return Book 1
#
# 5. Change Price of Book 1
#
# # 0. Exit



class Book:
    book_count=0
    book_issued=0
    def __init__(self,book_id,title,author,price):
        self.book_id=book_id
        self.title = title
        self.author = author
        self.price=price
        self.is_issued=False
        Book.book_count+=1
    def display(self):
        print("_________________BOOK MANAGEMENT_________________________")
        print(f"BOOK ID\t:{self.book_id}")
        print(f"TITLE\t:{self.title}")
        print(f"AUTHOR\t:{self.author}")
        print(f"PRICE\t:{self.price}")
        if (self.is_issued==False):
            print(f"STATUS\t:Available")
        else:
            print(f"STATUS\t:Not Available")
    def issue_book(self):
        if not self.is_issued:
            print("BOOK ISSUED SUCCESSFULLY")
            self.is_issued=True
            Book.book_issued+=1
        else:
            print("BOOK ALREADY ISSUED")
    def return_book(self):
        if self.is_issued:
            print("BOOK RETURNED SUCCESSFULLY")
            self.is_issued=False
            Book.book_issued -= 1
        else:
            print("BOOK NOT ISSUED YET")
    def change_price(self,new_price):
        if new_price>0:
            print("PRICE UPDATED SUCCESSFULLY")
            self.price=new_price
        else:
            print("ERROR")
book_id=int(input("ENTER THE BOOK_ID"))
title=input("ENTER THE BOOK TITLE")
author=input("ENTER THE BOOK AUTHOR")
price=int(input("ENTER THE PRICE"))
b1=Book(book_id,title,author,price)
book_id=int(input("ENTER THE BOOK_ID"))
title=input("ENTER THE BOOK TITLE")
author=input("ENTER THE BOOK AUTHOR")
price=int(input("ENTER THE PRICE"))
b2=Book(book_id,title,author,price)
option = int(input(
    "SELECT THE FOLLOWING OPTIONS\n"
    "1. DISPLAY BOOK 1\n"
    "2. DISPLAY BOOK 2 \n"
    "3. ISSUE BOOK 1\n"
    "4. RETURN BOOK 1 \n"
    "5. CHANGE PRICE OF THE BOOK 1 \n"
    "0. EXIT\n"
    "ENTER YOUR CHOICE: "
))
while option != 0:

    if option == 1:
        b1.display()

    elif option == 2:
        b2.display()

    elif option == 3:
        b1.issue_book()

    elif option == 4:
        b1.return_book()

    elif option == 5:
        new_price=int(input("ENTER THE PRICE"))
        b1.change_price(new_price)
    else:
        print("INVALID CHOICE")

    option = int(input("ENTER YOUR CHOICE: "))
print("THE NUMBER OF BOOK ISSUED ARE ",Book.book_count)

