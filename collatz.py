# coding=utf-8

'''
 The following iterative sequence is defined for the set of positive integers:
 n → n/2 (n is even)
 n → 3n + 1 (n is odd)

 Using the rule above and starting with 13, we generate the following sequence:

 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

 Which starting number, under one million, produces the longest chain?

'''

import os
import sys
import math
from timer import Timer

def max_collatz(limit):
	max_length = 1
	for number in xrange(2,limit+1):
		length = collatz(number)
#		print "max_collatz :", number, length, max_length
		if max_length < length:
			max_length = length
			max_number = number
	print "for upper limit %d , %d generates collatz of length %d" %(limit,max_number,max_length)


def collatz(number):
	length = 1
	while number != 1:
#		print "collatz :", number, length
		number = operation(number)
		length = length + 1
		if number == 1 :
			break
	return length


def operation(number) :
	if number == 1 :
		return 1
	elif number % 2 == 0 :
		return number / 2
	else :
		return 3 * number + 1


if __name__ == '__main__':
	print 'This utility prints the number Which producesthe longest chain obeying Collatz equalities'
	try:
		session = True
		while session:
			print "\n\nEnter the upper limit to find the longest chain. Enter 0 to exit ."
			upper_limit = raw_input()
			if upper_limit.isdigit():
				if int(upper_limit) == 0:
					session = False 
				else:
					with Timer() as t:
						max_collatz(int(upper_limit))
					print "=> elasped max_collatz: %s s" % t.secs
			else:
				print "Please enter a valid number . Enter 0 to exit "
	except:
		e = sys.exc_info()
		print e


