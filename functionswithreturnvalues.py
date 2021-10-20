def average(myList):
  total = sum(myList) # use the sum function
  average = total / len(myList) # len gives number of items
  return average

scores = [7, 23, 56, 89]
averageScore = average(scores)
print('The average of the scores is', averageScore)

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