#!/bin/python3

import math
import os
import random
import re
import sys

print('How many steps would you like your # staircase to have?\n')

# Complete the staircase function below.
while True: 
  def staircase(n):
      r = 1
      n = n -1
      while n >= 1:
          n = n - 1
          s = " " * n 
          d = "#" * r
          print(s, d)
          r = r + 1
      o = "#" * r
      print(o)

  def staircase2(n):
      num_sharps = 1
      while num_sharps <= n:
          s = " " * (n-num_sharps) + "#" * num_sharps
          num_sharps = num_sharps + 1
          print(s)
      print('Here is your staircase\n')

  def staircase3(n):
      num_spaces = n - 1
      num_sharps = 1
      while num_spaces >= 0:
          print(" " * num_spaces + "#" * num_sharps)
          num_spaces = num_spaces - 1
          num_sharps = num_sharps + 1

  if __name__ == '__main__':
      n = int(input())

      staircase2(n)