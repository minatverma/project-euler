# coding=utf-8


'''
The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
import os
import sys
import math

def all_trucateable_primes(count):
	counter = 0
	number = 11
	truncateable_prime_list = list()
	while counter < count:
		if is_prime(number):
			if is_left_truncateable_prime(number):
				if is_right_truncateable_prime(number):
					counter = counter + 1
					truncateable_prime_list.append(number)
		number = number + 2
	print truncateable_prime_list



def is_left_truncateable_prime(number) :
	length = len(str(number))
	for times in xrange(length-1):
		number = number % min_n_digit_number(length-times)
		if is_prime(number):
			continue
		else:
			return False
	return True

def is_right_truncateable_prime(number):
	for times in xrange(len(str(number))-1):
		number = number / 10
		if is_prime(number):
			continue
		else:
			return False
	return True

def min_n_digit_number(n):
	return 10 ** (n - 1)


def is_prime(number) :
	if number < 2:
		return False
	if number == 2 or number == 3:
		return True
	if number > 3 :
		for i in xrange (2 ,int(number ** 0.5)+1,2):
			if number % i == 0:
				return False
		return True



if __name__ == '__main__':
	print "This utility prints the user input Truncateable primes. Total 11 such numbers exist"
	try:
		session = True
		while session:
			print "\nHow many truncateable primes u wanna see ? . Enter 0 to exit"
			number = raw_input()
			if number.isdigit():
				number = int(number)
				if number == 0:
					session = False
					break
				if int(number) < 0 or int(number) > 11:
					print "only 11 such numbers exist . please enter value between 0 and 11"
					continue
				else:
					all_trucateable_primes(int(number))
			else:
				print "Please enter a valid number"
	except :
		e = sys.exc_info()
		print e





