names = ['alex', 'bob', 'sue', 'dave', 'emily']
for i in names:
  print('Welcome to the class,' i)



suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
cardno = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def make_cards():
  cards = []
 # start with empty list and add compile
  for s in suits:
    for i in cardno: # for each card number in each suit
      cards.append(i + '-' + s)
  return cards
my_cards = make_cards()
print(my_cards)  

x = Python
for i in x:
  print(i)