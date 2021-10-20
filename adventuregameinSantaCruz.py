# adventure game

import time

print('Welcome to Santa Cruz Mountain Adventure Game!')
print('**********************************************')
print('You are visiting Santa Cruz, California')
print('You go on an evening hike alone in the mountains')
print('You can pick one item to take with you -')
print('map(m), flashlight(f), chocolate(c), rope(r), or sticks(s): ')
item = input('What do you choose?: ') # choose an item
print('You hear a humming sound')
choice1 = input('Do you follow the sound? Enter y or n:\n')
while not (choice1 == 'y' or choice1 == 'n'): # follow or not
  choice1 = input('That is an invalid input. Enter y or n')
if choice1 == 'y': # yes, you follow the sound
  print('You keep moving closer to the sound')
  print('The sound suddenly stops')
  time.sleep(3)
  print('You are now LOST! ... ')
  time.sleep(3)
  print('You try to call on your phone, but there is no signal!')
  # choose direction
  direction = input('Which direction do you go? north, south, east, or west: ')
  if direction == 'north': # north
    print('You reached an abandoned cabin')
    if item == 'm': # need map
      print('You use the map to find your way home')
      print('CONGRATULATIONS! You won the game ')
    else: # lose without a map
      print('If you had a map, you could find your way from here')
      print('---You are still lost. You lost the game---')
  elif direction == 'south': # south
    print('You reach a river with a broken bridge.')
    if item == 'r' or item == 's': # need rope or sticks
      print('You choose an item that can fix the bridge')
      print('You fix the bridge, cross over, and find your way home')
      print('CONGRATULATIONS! You won the game')
    else: # lose without rope or sticks
      print('You if you had a rope or stick, you could fix the bridge')
      print('---You are still lost. You lost the game---')
  elif direction == 'west': # west, you lose
    print('You are walking and trip over a fallen log')
    print('You have hurt your foot. You sit down and wait for help')
    print('This could be a long time. You are still lost')
    print('---You are still lost. You lost the game---')
  else: # east
    print('You reach the side of the highway. It is dark')
    if item == 'f': # need flashlight
      print('You use the flashlight to signal')
      print('A car stops and gives you a ride home')
      print('CONGRATULATIONS! You won the game')
    else: # lose without a flashlight
      print('If you had a flashlight, you could signal for help')
      print('---You are still lost. You lost the game---')
else: # you do not follow the sound
  print('Good idea. You are not taking risks')
  print('You start walking back to the starting point.')
  print('You realize that you are now LOST! ')
  print('The sound is behind you and is getting louder. You panic! ')
  action= input('Do you start running (r), or do you stop to make a call(c)?: ') # call or run
  while action == 'c': # calling does not work, you have to run
    print('The call does not go through')
    action = input('Do you want to run (r), or try calling again (c)?:')
  print('You are running fast. The sound gets really loud\n...')
  print('A woman on an electric scooter comes up behind you')
  answer = input('She says, "Name my favorite computer programming language": ') # favorite prog. languange
  if answer.lower() == 'python': # python is the correct answer
    print('She says, "Yes, Python is my favorite programming language."')
    print('"If you have some chocolate, I can help you."')
    if item == 'c': # need chocolate
      print('Luckly you did choose correctly!')
      print('You give her the chocolate')
      print('SHe helps you get home')
      print('CONGRATULATIONS! You won the game')
    else: # lose without chocolate
      print('You should have chosen that chocolate!')
      print('She rides away, leaving you alone and lost.')
      print('You lost the game')
  else: # lose if answer is not python
    print('She did not like your answer')
    print('She rides away, leaving you lost')
    print('You lost the game.')