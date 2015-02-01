# coding=utf-8
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# time profile  : kernprof -l -v prime_of_rank.py
# memory profile: python -m memory_profiler prime_of_rank.py

import os
import sys
import math
from time import time

@profile
def prime_of_rank(rank) :
	current = 0
	number = 2
	start = time()
	while current < rank :
		if check_prime(number):
			current = current + 1
		if current == rank :
			break
		number = number + 1
	print number
	print "time taken in seconds", time() - start 

def check_prime(number) :
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
	print "\nThis utility helps in finding the prime number of user input Rank"
	try:
		session = True
		while session:
			print "\n\nEnter the Rank of prime number you want to see . Enter 0 to exit ."
			rank = raw_input()
			if rank.isdigit():
				if int(rank) == 0:
					session = False
				else:
					prime_of_rank(int(rank))
			else:
				print "Please enter a valid number . Enter 0 to exit "
	except  :
		e = sys.exc_info()
		print e
		
		