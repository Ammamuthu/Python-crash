import random

lst=["r","s","p"]
print("\n\t\t\t\t\t\t\t\t ROCK Papper SCICOOR Game \n")
print("\t rock = r\n")
print("\t paper = p\n")
print("\t sciccor =  s\n")
count=10
chance=0
man=0
robot=0
while chance< count:

    human=input("rock,paper,scissor : \t\t")
    comp=random.choice(lst)

    if human==comp:
        print("both are,so same tie 0 point \n")
    elif human=="r" and comp=="p":
        robot=robot+1
        print(f"computer has won 1 point\n")
        print(f"computer point is     {robot}       and your point is     {man}\n")
        print(f"your guess is       {human} and computer is      {comp}\n")

    elif human=="r" and comp=="s":
        man=man+1
        print(f"you have won 1 point\n")
        print(f"your point is     {man} and computer point is     {robot}\n")
        print(f"your selection is     {human} and computer slection is      {comp} \n")
    elif human=="p" and comp=="s":
        robot=robot+1
        print(f"computer has won 1 point\n")
        print(f"computer point is         {robot} and your point is       {man}\n")
        print(f"your guess is          {human} and computer is        {comp}\n")
    elif human=="p" and comp=="r":
        man=man+1
        print(f"you have won 1 point")
        print(f"your point is      {man} and computer point is        {robot}\n")
        print(f"your selection is       {human} and computer slection is           {comp}\n ")
    elif human=="s" and comp=="r":
        robot=robot+1
        print(f"computer has won 1 point")
        print(f"computer point is       {robot} and your point is        {man}")
        print(f"your guess is         {human} and computer is        {comp}")
    elif human=="s" and comp=="p":
        man=man+1
        print(f"you have won 1 point\n")
        print(f"your point is              {man} and computer point is             {robot}\n")
        print(f"your selection is         {human} and computer slection is      {comp}\n ")
    else:
        print ("you press a wrong key man \n")
        
        
        
    chance=chance+1
    print(f"{count-chance} is left out of {count}")
print("\n \t\t\t\t\t gave over")

if human==comp:
    print("both ar tie\n")
elif human>comp:
    print( "you are winner\n")
else:
    print("computer has won\n")
print(f"computer is       {man} and human is            {robot}")