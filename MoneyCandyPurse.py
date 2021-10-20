while True:
  print('I am going to take some notes on the things in.\nPlease answer the following questions.\n')
  purse = dict()

  purse['money'] = input('How much money in your purse?\n')
  while True:
    try:
      float(purse['money'])
      print('Thank you for putting in numbers for the amount of money you have in your purse.\n')
      break;
    except:
      purse['money'] = input('I ASKED you how much money you had.\n')

  purse['candy'] = input('How many candies in your purse?\n')
  while True:
    try:
      float(purse['candy'])
      print('Thank you for putting in numbers for the amount of candy you have in your purse.\n')
      break;
    except:
      purse['candy'] = input('I ASKED you how many candies you had.\n')

  purse['tissues']= input('How many tissues in your purse?\n')
  while True:
    try:
      float(purse['tissues'])
      print('Thank you for putting in numbers for the amount of tissues you have in your purse.\n')
      break;
    except:
      purse['tissues'] = input('I ASKED you how much tissues you had.\n')

  print('These are some of the things you had in your purse:', purse)