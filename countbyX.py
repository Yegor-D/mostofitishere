count = input('Enter number you want to count by: ')
count = int(count)
n = 0
userinput = input('Enter return to continue or q to quit:')
while not userinput == 'q':
  print(n)
  n = n + count
  userinput = input('Enter return to continue or q to quit: ')