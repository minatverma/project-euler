#coding=utf-8

import sys
import os
import math


def largest_prod_seq(array, number):
	max_seq = 0
	prod_seq = 0
	try:
		for rows in array :
			# print "rows, number",rows , len(rows)
			start_index = 0
			end_index = start_index + number - 1
			# print "start_index , end_index",start_index,end_index
			while end_index < len(rows):
				for a in range(start_index,end_index+1):
					prod_seq = prod_seq * rows[a]
				if prod_seq > max_seq:
					max_seq = prod_seq
					# print "sum, max",prod_seq,max_seq
				start_index = start_index + 1
				end_index = end_index + 1
				prod_seq = 1
				# print "si ,ei " ,start_index,end_index
		print "\n\n\tMax sum of %d consecutive number in array horizontally = %d" %(number, max_seq)
	except :
		e = sys.exc_info()
		print e


def set_up_array(grid):
	number_list = list()
	array_list = list()
	array = list()
	for row in grid:
		for a in row:
			if a.isdigit():
				number_list.append(a)
		array_list.append(number_list)
		number_list = []
	for arrays in array_list:
		array.append(map(int,arrays))
	print array
	return array
	# print number_list


if __name__ ==  "__main__":
	print """\nThis utility finds greatest product of four adjacent numbers in the
	 same direction in the file grid"""
	print "\nTo end session press 1 !!"
	try:
		if len(sys.argv) == 2:
			grid = open(sys.argv[1], 'rU')
		else :
			print "\n\nPlease provide source file for reading grid data"	
			exit(1)
		array = set_up_array(grid)
		session = True
		while session:
			print "\nEnter your number"
			number = raw_input()
			if number.isdigit():
				if int(number) == 1:
					session = False
				else:
					largest_prod_seq(array,int(number))
			else:
				print number, " is not a valid number.please try again.else print 1 to exit"
				continue
	except :
		e = sys.exc_info()
		print e
