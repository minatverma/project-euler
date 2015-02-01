# coding=utf-8
# Problem Statement
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import os
import sys
import re
import timeit

def larget_prime_factor(number):
	start = timeit.default_timer()
	factor_list = list()
	div = 2
	while div**2 < number :
		if number % div == 0:
			number = number / div
			if div not in factor_list:
				factor_list.append(div)
		else:
			div = div + 1
	if number not in factor_list:
		factor_list.append(number)
	print '\n Factor List = ', factor_list
	stop = timeit.default_timer()
	print 'Time : ', start - stop


if __name__ ==  "__main__":
	print "\nThis utility helps in finding disctinct factors of a number"
	print "To end session press 1 !!"
	try:
		session = True
		while session:
			print "\nEnter your number"
			number = raw_input()
			if number.isdigit():
				if int(number) == 1:
					session = False
				else:
					larget_prime_factor(int(number))
			else:
				print number, " is not a valid number.please try again.else print 1 to exit"
				continue
	except Exception:
		pass
