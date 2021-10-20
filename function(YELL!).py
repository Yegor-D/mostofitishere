# def yell(text):
#   return text.upper() + '!'
# >>> yell('hello')
# 'HELLO!'

# bark = woof
# bark('woof')

# del yel
# yell('hello?')
# #error will come
# bark('hey') will still work

# bark.__name__ command gives us 'yell''

# def greet(func):
#   greeting = func('Hi, I am a Python program')
#   print(greeting)

# greet(bark) command will capitalize what 'greet' does

# def whisper(text):
#   return text.lower() + '...'

# greet(whisper) returns a lowercase version of 'greet'

# list(map(bark, ['hello', 'hey', 'hi'])) will print HELLO! HEY! HI!

# def speak(text):
#   def whisper(t):
#     return t.lower() + '...'
#   return whisper(text)           # functions inside other functions
# 'whisper' does not exist outside of 'speak'

# def get_speak_func(volume):
#   def whisper(text):
#     return text.lower() + '...'
#   def yell(text):
#     return text.upper() + '!'
#   if volume > 0.5:
#     return yell
#   else:
#     return whisper

# speak_func = get_speak_func(0.7)
# speak_func('Hello')
# will give you 'HELLO!'

# def get_speak_func(text, volume):
#   def whisper():
#     return text.lower() + '...'
#   def yell():
#     return text.upper() + '!'
#   if volume > 0.5:
#     return yell
#   else:
#     return whisper
# >>> get_speak_func('Hello, World', 0.7)() will 'yell' Hello, World

# def make_adder(n):
#   def add(x):
#     return x + n
#   return add

# >>> plus_3 = make_adder(3)
# >>> plus_5 = make_adder(5)

# >>> plus_3(4) returns 7
# >>> plus_5(4) returns 9

# class Adder:
#   def __init__(self, n):
#     self .n = n
#   def __call__(self, x):
#     return self.n + x

# >>> plus_3 = Adder(3)
# >>> plus_3(4) still returns 7

# >>> add = lambda x, y: x + y
# >>> add(5, 3) returns 8

# def add(x, y):
#   return x + y
# >>> add(5, 3) does the same

# (lambda x, y: x + y)(5, 3)

# def make_adder(n):
#   return lambda x: x + n
# plus_3 = make_adder(3) adds 3 to something

# Harmful:
>>> list(filter(lambda x: x % 2 == 0, range(16)))
[0,2,4,6,8,10,12,14]
# Better:
>>> [x for x in range(16)ifx%2==0]
[0,2,4,6,8,10,12,14]

wrapper chapter in 3.3 in book python tricks

# • An is expression evaluates to True if two variables point to the same (identical) object.
# • An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).