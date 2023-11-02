import time
import datetime
print("------------ Welcome to G Lock---------------\n\n")
input("\t\t\t\t\tPress Any Key To Continue\n\n ")
def account():
    print("WELCOME TO SIGNIN Page")
    user_id=input("Creat an new ID for GLOCK  :  ")
    password=input("Enter your password  :  ")
    
    # def details():
    #     print (f" WELCOME TO {user_id})

    # print (f"IF YOU HAVE ACCOUNT PRESS --> Enter <--")
    # client=user_id
    # passs=passs
def profile():
    print("1. H o m e")
    print("2. S e c u r i t y ")
    print("3. D E - A c t i  v a t e d ")
    print("4. A B O U T U S")
    print("5. V E S I O N")
account()
# details()
profile()
customer=int(input("Enter the  optionl number that you want : "))
if customer==1:

    print(f"1 . C R E A T E L O C K")
    print(f"2 . A D D  A P P L I C A T I O N")
    print(f"3 .  E X I S T I N G   A P P")
    main=int(input("PRESS THE BUTTON THAT YOU WANT OPTIONAL  :  "))
    if main==1:
        
        print(" IF YOU HAVE AN ACCOUNT PRESS -->ENTER<--\n  \n ")
        input()
        # account()
    
    elif main==2:
        print (f"Select the application that you want : ")
    
        print("Facebook")
        print("whatsapp")
        print("instagram")
        print("Gallery")
        print("CALL")
        print("Google paay")
        print("Youtube")
        app=input("Enter the Name : ")
    elif main==3:
        app=input("in your device" )
        print (f"APP selected {app} on {time.localtime()}")

elif customer==2:
    print("<---------- SECURITY--------------->")
    print (f" select lock type : camera,voice,fscanner ")
elif customer==3:
    print (f"Welcome MR")
elif customer==4:
    print(" aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
elif customer==5:
    print(" drain fafnier")


else:
    print("INVALID OPTION")