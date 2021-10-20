def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


while True:
  number = input('number\n')
  int(number)
  number = int(number)

  print(factorial(number))