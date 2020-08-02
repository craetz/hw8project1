# Exercise No.  1
# File Name:    hw8project1.py 
# Programmer:   Cory Raetz
# Date:         July 16, 2020
#
# Problem Statement: This program calculates the nth number when given a position provided by the user
#
#
# Overall Plan:
# 1. Calculate phi
# 2. Prompt user to input value of n
# 3. Calculate nth number
#
#

import math

phi = 0.5+((math.sqrt(5))/2)

print("This program calculates the value of a number in the Fibonacci sequence at a given position.")
n = eval(input("\nPlease enter the position of the Fibonacci number to calculate: "))

if n==0:
  print("\nWhen n = 0, the value of the Fibonacci number = ",0)
elif n==1:
  print("\nWhen n = 1, the value of the Fibonacci number = 1")
elif n==2:
  print("\nWhen n = 1, the value of the Fibonacci number = 1")
else:
  nth = ((phi**n)-((1-phi)**n))/math.sqrt(5)

  print("\nWhen n =",n,", the value of the Fibonacci number =",int(nth))


