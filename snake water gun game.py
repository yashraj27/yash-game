                                          #SNAKE WATER GUN GAME

import random
chance:int=5
number_of_chance: int=0
youWon:int=0
cmpWon:int=0
lst= ["snake","water","gun"]
random.choice(lst)


while number_of_chance<chance:
    chos = input("\nenter your choice as snake, water,gun")
    number_of_chance += 1

    if chos==random.choice(lst):
        print("1.tye same choice")

    elif chos=="snake" and random.choice(lst)=="water":
        print("2.you won")
        youWon+=1

    elif chos=="snake" and random.choice(lst)=="gun":
        print("3.you loose")
        cmpWon+=1

    elif chos=="water" and random.choice(lst)=="snake":
        print("4.you losse")
        cmpWon += 1

    elif chos=="water" and random.choice(lst)=="gun":
        print("5.you won")
        youWon += 1

    elif chos=="gun" and random.choice(lst)=="snake":
        print("6.you won")
        youWon += 1

    elif chos=="gun" and random.choice(lst)=="water":
        print("7.you loose")
        cmpWon += 1
    else:
         print("enter correct choice")
if youWon>cmpWon:
    print("you was corret",youWon,"number of times")
    print("\t\t\t\tyou are the winner")
else:
    print("you was wrong", cmpWon, "number of times")
    print("\t\t\t\tyou loose")

