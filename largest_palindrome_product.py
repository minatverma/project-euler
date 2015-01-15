# coding=utf-8
# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import os
import sys
import math
import timeit

def largest_palindrome(length):
	if length == 2 :
		max = 99 
		min = 10
	if length == 3 :
		max = 999
		min = 100
	if length == 4 :
		max = 9999
		min = 1000
	max_palindrome = 0
	factor_list = list()
	for a in range(max,min,-1):
		for b in range(max,min,-1):
			num = a*b
			if check_palindrome(str(num)):
				if num > max_palindrome:
					max_palindrome = num
					factor_list = [a,b]
					break

	print 'largest palindrome made from the product of two %d-digit numbers is %d for %d and %d' \
	%(length,max_palindrome,factor_list[0],factor_list[1])


def check_palindrome(input):
	return input == input[::-1]

if __name__ ==  "__main__":
	print "\nThis utility helps in finding largest palindrome made from the product of two n-digit numbers"
	print "Where n = 2,3,4 !! The Program will exit for any other value"
	try:
		session = True
		while session:
			print "\nEnter your number length\n"
			number = raw_input()
			if number.isdigit():
				if int(number) not in [2,3,4]:
					session = False
				else:
					largest_palindrome(int(number))
			else:
				print number, " is out of range"
				continue
	except Exception:
		print "exception occurred"
		pass
