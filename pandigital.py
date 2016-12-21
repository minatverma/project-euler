#coding='utf-8'
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
import os
import sys
import math
import itertools

def largest_prime_pandigital():
  list = ['1','2','3','4','5','6','7','8','9']
  for a in itertools.permutations(list):
    number = ''.join(a)
    if is_pandigital(number) and is_prime(number):
        print 'pandigital number', number
        break
        
def is_pandigital(number):
  length = len(str(number))
  number_array = []
  for a in str(number):
    number_array.append(a)
  for a in xrange(1,length+1):
    if str(a) not in number_array:
      return False
  return True
  

def is_prime(input) :
  number = int(input)
  if number < 2:
    print "Not applicable to this number"
  if number == 2 or number == 3:
    return True
  if number > 3 :
    for i in xrange (2 ,int(number ** 0.5)+1,1):
      if number % i == 0:
        return False
  return True


if __name__ == "__main__":
  try:
    largest_prime_pandigital()
  except  :
    e = sys.exc_info()
    print e
