import random
import time

def roll_dice(n):
  dice = [] #start with an empty list of dice
  #add random numbers between 1 to 6 to the list
  for i in range(n):
    dice.append(random.randint(1,6))
  return dice

def find_winner(cdice_list, udice_list):
  computer_total = sum(cdice_list)
  user_total = sum(udice_list)
  print('Computer total', computer_total)
  print('User total', user_total)
  if user_total > computer_total:
    print('User wins')
  elif user_total < computer_total:
    print('Computer wins')
  else:
    print('It is a tie')

def roll_again(choices, dice_list):
  print('Rolling again ...')
  time.sleep(3)
  for i in range(len(choices)):
    if choices[i] == 'r':
      dice_list[i] = random.randint(1,6)
  time.sleep(3)

def computer_strategy1(n):
  # create computer choices : Roll everything again
  print('Computer is thinking ...')
  time.sleep(3)
  choices = '' # start with an emty list of choices
  for i in range(n):
    choices = choices + 'r'
  return choices

def computer_strategy2(n):
  # create computer choices: roll if < 5
  print('Computer is thinking... ')
  time.sleep(3)
  choices = '' # start with an empty list of choices
  for i in range(n):
    if computer_rolls[i] < 5:
      choices = choices + 'r'
    else:
      choices = choices + '-'
  return choices

# step one - start game
number_dice = input('Enter number of dice: ')
number_dice = int(number_dice)
ready = input('Ready to start? Press any key to continue')

# step 2 in main program area - roll number_dice
# user turn to roll
user_rolls = roll_dice(number_dice)
print('User first roll: ', user_rolls)

# step 4 - get user choices
user_choices = input('Enter - to hold or r to roll again: ')
# check length of user input
while len(user_choices) != number_dice:
  print('You must enter', number_dice, 'choices')
  user_choices = input('Enter - hold or r to roll again: ')

# step 5 - roll again based on user choices
roll_again(user_choices, user_rolls)
print('Player new ROll: ', user_rolls)


# computers turn to roll
print('Computers turn ')
computer_rolls = roll_dice(number_dice)
print('Computer first roll: ', computer_rolls)

# step 6
# decide on what choice - using one of the strategy funcionts
computer_choices = computer_strategy2(number_dice)
print('Computer Choice: ', computer_choices)
# computer rolls again using the choices it made
roll_again(computer_choices, computer_rolls)
print('Computer new roll: ', computer_rolls)

find_winner(computer_rolls,user_rolls)