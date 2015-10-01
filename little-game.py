#!/usr/bin/env python
# -*- coding: utf-8 -*-


again = True
while again == True:
    lower_limit = int(input("please input the lower limit:"))
    upper_limit = int(input("please input the upper limit:"))
    from random import randint
    num = randint(lower_limit,upper_limit)
    time = 0

    print("guess what I think")
    bingo = True

    while bingo == True:
        time += 1
        answer = int(input("please input number:"))

        if answer < num:
            print("%d is too small"%answer)

        if answer > num:
            print("%d is too big"%answer)
            
        if answer == num:
            print("bingo,%d is the right answer"%answer)
            print("you have try %d times!"%time)
            time = 0

            print("play again?")
            y = True
            n = False
            
            judge = True
            while judge == True:
                
                choice = input ("please input y or n:")
                if choice == "y":
                    bingo = False
                    judge = False
                   
                elif choice == "n":
                    again = False
                    bingo = False
                    judge = False
                    print("end")