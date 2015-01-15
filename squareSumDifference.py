# coding=utf-8
# difference between the sum of the squares of the first one hundred natural numbers and the square of the sum


def square_sum_difference(n):
	diff = (n * (n + 1) * (3*n*n - n - 2)) / 12
	print "Difference for 1st %d numbers is %d"%(n , diff)


if __name__ ==  "__main__":
	print """\nThis utility helps in finding difference between the sum 
	\t\tof the square of the sum of first one hundred natural numbers and the square of the sum"""
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
					square_sum_difference(int(number))
			else:
				print number, " is not a valid number.please try again.else print 1 to exit"
				continue
	except Exception:
		pass
