# coding=utf-8

import os
import sys
import math


def pythagorean_triplet():
	a = 3
	b = 4
	c = 5
	n = math.ceil((1000) / (a + b + c))
	print "Triplets : ", n*a , n*b, n*c 
	print "sum : " , n*(a+b+c)
	print "product : " ,n*n*n*a*b*c

if __name__ == "__main__":
	pythagorean_triplet()

