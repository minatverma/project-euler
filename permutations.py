#coding=utf-8


import os
import sys
from itertools import permutations
import math


def permutation(series, number):
	permutation_generator = permutations(series,r=number)
	print "Enter index of permutation you want"
	index = int(raw_input())
	print list(map("".join,permutation_generator))[index]


def make_series(array):
	series = list()
	for a in array:
		if a.isdigit() and a not in series:
			series.append(a)
	# print series
	return series


if __name__ ==  "__main__":
	print "\nThis utility helps in finding nth Permutation of a series"
	try:
		session = True
		while session:
			print "\nEnter your array. Enter 0 to exit"
			array = raw_input()
			if array == '0':
				session = False
				break
			if len(array) < 2:
				print "Enter at least 2 distinct numbers"
				break
			else:
				series = make_series(array)
			print "Enter rank :"
			number = raw_input()
			if number.isdigit():
				if int(number) > len(series):
					print "Enter between 2 and ", len(series)
				else:
					permutation(series,int(number))
	except :
		e = sys.exc_info()
		print e
