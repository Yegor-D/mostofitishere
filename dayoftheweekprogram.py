# day of the week program
day = input('Enter day of the week')
if day == 'monday' or day == 'wednesday':
  alarm = '7.30am'
  carpool = True
  coding_class = True
  gym = False
elif day == 'tuesday' or day == 'thursday':
  alarm = '7.30am'
  carpool = False
  coding_class = False
  gym = True
elif day == 'friday':
  alarm = '6.30am'
  carpool = True
  coding_class = False
  gym = False
else:
  alarm = 'OFF'
  carpool = False
  coding_class = False
  gym = True
print(alarm, carpool, coding_class, gym)