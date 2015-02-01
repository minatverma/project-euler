# coding=utf-8

# time profile  : kernprof -l -v number_nth_power.py
# memory profile: python -m memory_profiler number_nth_power.py

'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

import os
import sys

@profile
def number_nth_power(power):
	power_list = list()
	roof = (power+1) * (9 ** power)
	for number in range(2,roof):
		if is_nth_power(number, power):
			power_list.append(number)
	print power_list, sum(power_list)

@profile
def is_nth_power(number, power):
	total = 0
	temp = number
	for times in xrange (len(str(number))):
		total = total + ((temp % 10) ** power)
		temp = temp / 10
	if number == total:
		return True
	else :
		return False


if __name__ == "__main__":
	print "\nThis utility helps in finding SUM of numbers which can be expressed as nth Power of their digits."
	try:
		session = True
		while session:
			print "\n\nEnter the Power. Enter 0 to exit ."
			power = raw_input()
			if power.isdigit():
				if int(power) == 0:
					session = False
				else:
					number_nth_power(int(power))
			else:
				print "Please enter a valid number . Enter 0 to exit "
	except  :
		e = sys.exc_info()
		print e
		
		