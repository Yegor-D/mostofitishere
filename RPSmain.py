# copy and paste this code into the first line of main.py, before all the other code there (if there is any).

import RPSelements
import random
import click
def clrscr():
   # Clear screen using click.clear() function
    click.clear()
print(RPSelements.welcome)
play="Y"
while play=="Y" or play=="y":
  choice=int(input("Enter Your Choose:\nType 0 for Rock , 1 for Paper , 2 for scissors:\n)> "))
  print("Your choice:")
  if choice==0:
    print(RPSelements.rock)
  elif choice==1:
    print(RPSelements.paper)
  elif choice==2:
    print(RPSelements.scissors)
  else:
    print("Kindly enter an Valid Number 0 , 1 , 2 only")
  print("Computer's choice :")
  choice_computer=random.randint(0,2)
  if choice_computer==0:
    print(RPSelements.rock)
  elif choice_computer==1:
    print(RPSelements.paper)
  elif choice_computer==2:
    print(RPSelements.scissors)
  string_choice=str(choice)
  string_choice_computer=str(choice_computer)
  num=string_choice+string_choice_computer
  if num=="02"or num=="10"or num=="21":
    print("You Won :) , Have a lucky Day Ahead")
  elif num=="00"or num=="11" or num=="22":
      print("It's a Tie :| , You are a Tough Opponent")
  else:
    print("You lost better luck next time ")
  print("\r")
  play=input("Do you want to play again.\nIf Yes then type : 'Y' , if u want to exit type 'N':\n)> ")
  clrscr()
print("\r")
print("Thanks For Playing , Come Back Soon :)")