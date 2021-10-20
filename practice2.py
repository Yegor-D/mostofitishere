raining = True
if raining:
  print('It is wet outside')
  print('Wear rain boots')
  print('Take an umbrella')

day = input('enter day of the week')

if day == 'saturday' or day == 'sunday':
  alarm = 'OFF'
  print('It is a weekend - sleep in!')

else:
  alarm = 'ON'
  print('Get up and get ready for work')