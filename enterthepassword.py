password = 'secret987'
userpass = input('Enter the password: ')
while not password == userpass:
  print('Try again')
  userpass = input('Enter the password: ')
print('Correct')