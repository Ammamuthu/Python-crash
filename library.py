
from time import sleep

import webbrowser

import time

class Library:

    def __init__(self,book,name):

        self.list_of_books=book

        self.library_name=name

    def show_books(self):

        print("Books present in th library is :-")

        count=1

        for booksName in self.list_of_books:

            print(f"{count}.{booksName}")

            count+=1

    def member_ship(self):

        print("Did u sunscribe Codina anna youtube channel ?")

        youtube=input("yes or no :")

        if youtube =="yes":

            print("you are allowed to buy membership !!")

            print("Did u have member ship or not ?")

            member=input("Enter yes or no : ")

            if member=="yes":

                print("you can take the book !!!")

            elif member =="no":

                print("You have to buy membership to take the books to home")

                print("do u want to buy member ship ?")

                buy_memeber=input("yes or no :")

                if buy_memeber=="yes":

                    global membreship_name

                    membreship_name=input("Enter the name :")

                    print(f"thank you {membreship_name} for buy membership !!! ,Now u can able to take books to Home 😀😀😀😀")

        else:

            print("idot u dont have permison first sunscribe his channel and come back 😡😡😡😡")

            sleep(3)

            webbrowser.open("https://www.youtube.com/channel/UCvkL4BczzmIeGUKM7Sz2drg")

                

    def lent_book(self):

            global book_name,membreship_name

            books.show_books()

            book_name=input("Enter the book name to lend from above list:")

            name=input("Enter the registration name:")

            try:

                if membreship_name==name:

                    if book_name in self.list_of_books:

                        print(f"You have been issued {book_name}. Please keep it safe and return it within 15 days")

                        self.list_of_books.remove(book_name)

                        return self.list_of_books

                    else:

                        return f"The book you asked was not there,sorry for it"

                    

                else :

                    print("sorry u dont have permision to take books to home")

            except:

                print("you dont have membership buy membership first")

    def lend_book_details(self):

        try:

            global membreship_name,book_name

            membreship_details={}

            membreship_details [f'{membreship_name}']=f'{book_name}'

            for key,value in membreship_details.items():

                print(f"name:{key}")

                print(f"book:{value}")

        except:

            print("no one has membership")

            

       

                

        

    def return_book(self):

        global book_name,membreship_name

        return_book=input("Enter the book to be returned :")

        if book_name== return_book:

            print(f"book is returned succesfully by {membreship_name}")

            self.list_of_books.append(return_book)

        else:

            print("u have entered wrong book name:")

            

    def add_book(self):

        add_book=input("Enter the book to add :")

        self.list_of_books.append(add_book)

        print("your book has be added succesfuly !!!")

    def remove_book(self):

        books.show_books()

        remove_book=input("Enter the book name to be removed for above list:")

        self.list_of_books.remove(remove_book)

        print("The book has be removed succesfully !!")

    def buy_book(self):

        print('''

                 1.python-100$

                 2.Game development-80$

                 3.Web Development-120$ ''')

        buy=input("Enter the book name to buy :").lower()

        if buy=="python" or "game development" or "web development":

            print("thanks for buying sir")

    

            

                

# if name == "__main__":            

    books=Library(["python","java","c#","HTML & CSS"],"magesh")



    while True:

        print(f"-------------- Welcome to {books.library_name} Library ----------------------")

        print('''Please choose an option:

        1. List all the books

        2.Buy Membersip for lending book

        3.lend book

        4.lend a book details

        5.Add  a book

        6.Return a book

        7.remove book

        8.buy books

        ''')

        choice=int(input("Enter the number :"))



        if choice ==1:

            books.show_books()

        elif choice ==2:

            books.member_ship()

        elif choice ==3:

            books.lent_book()

        elif choice ==4:

            books.lend_book_details()

        elif choice ==5:

            books.add_book()

        elif choice==6:

            books.return_book()

        elif choice==7:

            books.remove_book()

        elif choice==8:

            books.buy_book()



        else:

            print("invalid choice !!")

        condition=input("------------------------Enter q to exist or c to contine ------------------------:")

    

        if condition=="q":

            print("Thankyou for coming to our library !!")

            exit()

        elif condition == "c": 

            continue

        else:

            print("You have entered wrong choice")

            break