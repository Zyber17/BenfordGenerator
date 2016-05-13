import sys
from math import log10
from random import random

def benfordWrapper(digits):
	num = 0
	for i in range(1,digits + 1):
		num += benford(i) * 10**(digits - i)
	return num

def benford(digit):
	dist = [float(0)] * 10
	if digit == 1:
		for i in range(1,10):
			dist[i] = log10(1 + 1/float(i))
	else:
		for i in range(0,10):
			j = 10**(digit - 2)
			high = 10**(digit - 1)
			while j < high:
				val = float(1 + 1/(10 * j + float(i)))
				dist[i] += log10(val)
				j+=1
	rand = random()
	numsum = dist[0]
	i = 0
	while rand > numsum:
		i += 1
		numsum += dist[i]
	return i

if len(sys.argv) != 2:
	print 'You must provide the number of digits you want the number to be. If you want a five-digit number, try running `benford.py 5`.'
else:
	print benfordWrapper(int(sys.argv[1]))
