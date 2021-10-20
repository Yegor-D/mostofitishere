money = input('How much money do you have?')
indebt = input('Are you in debt?').lower()

if int(money) > 20 and indebt == 'no':
  print('good. that means you can buy some bread. Would you like to buy some bread?')
  buybread = input('').lower()
  if buybread == 'yes':
    print('You balance is now', int(money) - 20)
else:
  print("Sorry, you can't buy bread at this time")